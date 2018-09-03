import falcon
from falcon_cors import CORS
from aa.web_api import IpcTrackerResource
from aa.web_api import LandBattleResource
from aa.web_api import SimulationResource
from aa.web_api import UnitInfoResource


def create_application():
    cors = CORS(allow_all_origins=True, allow_all_headers=True,
                allow_all_methods=True, allow_credentials_all_origins=True)
    app = falcon.API(middleware=[cors.middleware])
    app.add_route('/ipc-tracker', IpcTrackerResource())
    app.add_route('/land-battle', LandBattleResource())
    app.add_route('/unit-info', UnitInfoResource())
    app.add_route('/', SimulationResource())
    return app


application = create_application()
