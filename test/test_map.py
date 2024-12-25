import unittest
from collections import defaultdict
from util.map import Map
from util.coordinate import Coordinate
from model.buildings.town_center import TownCenter
from model.units.villager import Villager

class TestMapCoordinate(unittest.TestCase):

    def setUp(self):
        self.map = Map(5)
        self.building = TownCenter()
        self.unit = Villager()
        self.building.set_coordinate(Coordinate(0, 0))
        self.unit.set_coordinate(Coordinate(4, 4))
    
    def tearDown(self):
        self.map = None
        self.building = None
        self.unit = None

    def test_get_size(self):
        self.assertEqual(self.map.get_size(), 5, "The map size should be 5")

    def test_add_building(self):
        self.map.add(self.building, Coordinate(0, 0))
        for x in range(5):
            for y in range(5):
                if x < 4 and y < 4:
                    self.assertEqual(self.map.get(Coordinate(x, y)), self.building, f"The building should be at position ({x}, {y})")
                else:
                    self.assertIsNone(self.map.get(Coordinate(x, y)), f"There should be no building at position ({x}, {y})")

    def test_add_unit(self):
        self.map.add(self.unit, Coordinate(4, 4))
        for x in range(5):
            for y in range(5):
                if x == 4 and y == 4:
                    self.assertEqual(self.map.get(Coordinate(x, y)), self.unit, f"The unit should be at position ({x}, {y})")
                else:
                    self.assertIsNone(self.map.get(Coordinate(x, y)), f"There should be no unit at position ({x}, {y})")

    def test_remove_building(self):
        self.map.add(self.building, Coordinate(0, 0))
        self.map.remove(Coordinate(0, 0))
        for x in range(5):
            for y in range(5):
                self.assertIsNone(self.map.get(Coordinate(x, y)), f"There should be no building at position ({x}, {y})")

    def test_remove_unit(self):
        self.map.add(self.unit, Coordinate(4, 4))
        self.map.remove(Coordinate(4, 4))
        for x in range(5):
            for y in range(5):
                self.assertIsNone(self.map.get(Coordinate(x, y)), f"There should be no unit at position ({x}, {y})")

    def test_move_unit(self):
        self.map.add(self.unit, Coordinate(4, 4))
        self.map.move(self.unit, Coordinate(4, 3))
        self.unit.set_coordinate(Coordinate(4, 3))
        for x in range(5):
            for y in range(5):
                if x == 4 and y == 3:
                    self.assertEqual(self.map.get(Coordinate(x, y)), self.unit, f"The unit should be at position ({x}, {y})")
                else:
                    self.assertIsNone(self.map.get(Coordinate(x, y)), f"There should be no unit at position ({x}, {y})")
        with self.assertRaises(ValueError):
            self.map.move(self.unit, Coordinate(0, 0))

    def test_get_method(self):
        self.map.add(self.building, Coordinate(0, 0))
        self.map.add(self.unit, Coordinate(4, 4))
        for x in range(5):
            for y in range(5):
                if x < 4 and y < 4:
                    self.assertEqual(self.map.get(Coordinate(x, y)), self.building, f"The building should be at position ({x}, {y})")
                elif x == 4 and y == 4:
                    self.assertEqual(self.map.get(Coordinate(x, y)), self.unit, f"The unit should be at position ({x}, {y})")
                else:
                    self.assertIsNone(self.map.get(Coordinate(x, y)), f"There should be no unit at position ({x}, {y})")
    
    def test_get_map(self):
        expected = defaultdict( lambda: None )
        for x in range(4):
            for y in range(4):
                expected[Coordinate(x, y)] = self.building
        expected[Coordinate(4, 4)] = self.unit
        self.map.add(self.building, Coordinate(0, 0))
        self.map.add(self.unit, Coordinate(4, 4))
        self.assertEqual(self.map.get_map(), expected, "The map should contain the building and the unit")
    
    def test_get_map_list(self):
        expected = [ [ self.building if i < 4 and j < 4 else None for j in range(5) ] for i in range(5) ]
        expected[4][4] = self.unit
        self.map.add(self.building, Coordinate(0, 0))
        self.map.add(self.unit, Coordinate(4, 4))
        self.assertEqual(self.map.get_map_list(), expected, "The map should contain the building and the unit")

    def test_get_from_to(self):
        expected = Map(5)
        expected.add(self.building, Coordinate(0, 0))
        expected.add(self.unit, Coordinate(4, 4))
        self.map.add(self.building, Coordinate(0, 0))
        self.map.add(self.unit, Coordinate(4, 4))
        self.assertEqual(self.map.get_from_to(Coordinate(0, 0), Coordinate(4, 4)).get_map(), expected.get_map(), "The map should contain the building and the unit")

    def test_get_map_from_to(self):
        expected = defaultdict( lambda: None )
        for x in range(2, 4):
            for y in range(2, 4):
                expected[Coordinate(x, y)] = self.building
        expected[Coordinate(4, 4)] = self.unit
        self.map.add(self.building, Coordinate(0, 0))
        self.map.add(self.unit, Coordinate(4, 4))
        self.assertEqual(self.map.get_map_from_to(Coordinate(2, 2), Coordinate(4, 4)), expected, "The map should contain the building and the unit")

    def test_get_map_list_from_to(self):
        expected = [ [ self.building if i >= 2 and i < 4 and j >= 2 and j < 4 else None for j in range(5) ] for i in range(5) ]
        expected[4][4] = self.unit
        self.map.add(self.building, Coordinate(0, 0))
        self.map.add(self.unit, Coordinate(4, 4))
        self.assertEqual(self.map.get_map_list_from_to(Coordinate(2, 2), Coordinate(4, 4)), expected, "The map should contain the building and the unit")

if __name__ == '__main__':
    unittest.main()