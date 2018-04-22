# from .unit import unit_factory
# from .utils import build_army
#
#
# def test_build_army():
#     config = {
#         'infantry': 2,
#         'tank': 1
#     }
#     army = build_army(config=config, unit_factory=unit_factory)
#     infantry_count = 0
#     tank_count = 0
#     for unit in army:
#         if unit.name == 'Infantry':
#             infantry_count += 1
#         if unit.name == 'Tank':
#             tank_count += 1
#     assert infantry_count == 2
#     assert tank_count == 1
