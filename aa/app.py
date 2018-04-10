import falcon
from falcon_cors import CORS
from aa.api import SimulationResource
from aa.api import UnitInfoResource
from aa.battle import simulate
from aa.unit.utils import build_army


cors = CORS(allow_all_origins=True, allow_all_headers=True,
            allow_all_methods=True, allow_credentials_all_origins=True)
application = falcon.API(middleware=[cors.middleware])

unit_info_resource = UnitInfoResource()
simulation_resource = SimulationResource(army_builder=build_army,
                                         battle_simulator=simulate)

application.add_route('/unit-info', unit_info_resource)
application.add_route('/', simulation_resource)
