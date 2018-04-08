import falcon
from aa.api import SimulationResource
from aa.api import UnitInfoResource
from aa.battle import simulate
from aa.unit.utils import build_army


application = falcon.API()

unit_info_resource = UnitInfoResource()
simulation_resource = SimulationResource(army_builder=build_army,
                                         battle_simulator=simulate)

application.add_route('/unit-info', unit_info_resource)
application.add_route('/', simulation_resource)
