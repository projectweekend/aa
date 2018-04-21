import falcon
from falcon_cors import CORS
from aa.battle import simulate
from aa.unit.utils import build_army
from aa.web_api import SimulationResource
from aa.web_api import UnitInfoResource


def create_application():
    cors = CORS(allow_all_origins=True, allow_all_headers=True,
                allow_all_methods=True, allow_credentials_all_origins=True)
    return falcon.API(middleware=[cors.middleware])


application = create_application()

unit_info_resource = UnitInfoResource()
simulation_resource = SimulationResource(army_builder=build_army,
                                         battle_simulator=simulate)

application.add_route('/unit-info', unit_info_resource)
application.add_route('/', simulation_resource)
