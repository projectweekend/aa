from marshmallow import Schema, fields, validates, ValidationError


class CreateSchema(Schema):

    name = fields.Str(required=True)
    starting_ipc = fields.Integer(required=True)

    @validates('starting_ipc')
    def _validate_starting_ipc(self, starting_ipc):
        if starting_ipc < 0:
            raise ValidationError('Quantity must be greater than 0')
