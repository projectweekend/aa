from datetime import datetime
from uuid import uuid4

import falcon

from aa.web_api.schema.ipc_tracker import CreateSchema, ValidationError


class IpcTracker:

    def __init__(self, game_id, name, created_at, starting_ipc):
        self.game_id = game_id
        self.name = name
        self.created_at = created_at
        self.starting_ipc = starting_ipc

    @classmethod
    def new(cls, name, starting_ipc):
        return cls(game_id=uuid4().hex, name=name,
                   created_at=datetime.utcnow(), starting_ipc=starting_ipc)

    def to_dict(self):
        out = {}
        for k, v in self.__dict__.items():
            if isinstance(v, datetime):
                out[k] = int(v.timestamp())
                continue
            out[k] = v
        return out


class IpcTrackerResource:

    def __init__(self, create_schema=CreateSchema):
        self.create_schema = create_schema

    def on_post(self, req, res):
        res.status = falcon.HTTP_201
        payload = self._validate_create(payload=req.media)
        tracker = IpcTracker.new(**payload)
        res.media = tracker.to_dict()

    def _validate_create(self, payload):
        try:
            new_game = self.create_schema().load(payload)
        except ValidationError as err:
            title = 'Invalid IPC Tracker new game request'
            desc = str(err.messages)
            raise falcon.HTTPBadRequest(title=title, description=desc)
        return new_game.data
