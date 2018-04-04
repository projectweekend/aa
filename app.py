import falcon
from api import SimulationResource
from battle import simulate
from unit.utils import build_army


application = falcon.API()

simulation_resource = SimulationResource(army_builder=build_army,
                                         battle_simulator=simulate)
application.add_route('/', simulation_resource)
