import unittest
from util.coordinate import Coordinate

class TestCoordinate(unittest.TestCase):
    def setUp(self):
        self.coordinate = Coordinate(1, 1)
    
    def tearDown(self):
        self.coordinate = None

    def test_set_x(self):
        self.coordinate.set_x(2)
        self.assertEqual(self.coordinate.get_x(), 2, "The x coordinate should be 2")
    
    def test_set_y(self):
        self.coordinate.set_y(2)
        self.assertEqual(self.coordinate.get_y(), 2, "The y coordinate should be 2")
    
    def test_get_x(self):
        self.assertEqual(self.coordinate.get_x(), 1, "The x coordinate should be 1")

    def test_get_y(self):
        self.assertEqual(self.coordinate.get_y(), 1, "The y coordinate should be 1")

    def test_distance(self):
        self.assertEqual(self.coordinate.distance(Coordinate(1, 1)), 0, "The distance should be 0")
        self.assertEqual(self.coordinate.distance(Coordinate(1, 2)), 1, "The distance should be 1")
        self.assertEqual(self.coordinate.distance(Coordinate(2, 1)), 1, "The distance should be 1")
        self.assertEqual(self.coordinate.distance(Coordinate(2, 2)), 2**0.5, "The distance should be 2**0.5")

    def test_is_in_range(self):
        self.assertTrue(self.coordinate.is_in_range(Coordinate(1, 1), 0), "The distance should be in range")
        self.assertTrue(self.coordinate.is_in_range(Coordinate(1, 2), 1), "The distance should be in range")
        self.assertTrue(self.coordinate.is_in_range(Coordinate(2, 1), 1), "The distance should be in range")
        self.assertTrue(self.coordinate.is_in_range(Coordinate(2, 2), 2**0.5), "The distance should be in range")
        self.assertFalse(self.coordinate.is_in_range(Coordinate(2, 3), 2**0.5), "The distance should not be in range")
    
    def test_is_adjacent(self):
        for x in range(4):
            for y in range(4):
                if x == 1 and y == 1:
                    self.assertFalse(self.coordinate.is_adjacent(Coordinate(x, y)), f"The coordinates should not be adjacent to itself")
                elif abs(x - 1) <= 1 and abs(y - 1) <= 1:
                    self.assertTrue(self.coordinate.is_adjacent(Coordinate(x, y)), f"The coordinates ({x}, {y}) should be adjacent")
                else:
                    self.assertFalse(self.coordinate.is_adjacent(Coordinate(x, y)), f"The coordinates ({x}, {y}) should not be adjacent")

    def test_hash(self):
        self.assertEqual(hash(self.coordinate), hash((1, 1)), "The hash should be equal to the tuple")
    
    def test_eq(self):
        for x in range(4):
            for y in range(4):
                if x == 1 and y == 1:
                    self.assertEqual(self.coordinate, Coordinate(x, y), f"The coordinates should be equal to itself")
                else:
                    self.assertNotEqual(self.coordinate, Coordinate(x, y), f"The coordinates should not be equal to ({x}, {y})")

    def test_lt(self):
        for x in range(4):
            for y in range(4):
                if x < 1 and y < 1:
                    self.assertLess(self.coordinate, Coordinate(x, y), f"The coordinates ({x}, {y}) should be less than (1, 1)")
                else:
                    self.assertFalse(self.coordinate < Coordinate(x, y), f"The coordinates ({x}, {y}) should not be less than (1, 1)")

    def test_le(self):
        for x in range(4):
            for y in range(4):
                if x <= 1 and y <= 1:
                    self.assertLessEqual(self.coordinate, Coordinate(x, y), f"The coordinates ({x}, {y}) should be less than or equal to (1, 1)")
                else:
                    self.assertFalse(self.coordinate <= Coordinate(x, y), f"The coordinates ({x}, {y}) should not be less than or equal to (1, 1)")
    
    def test_gt(self):
        for x in range(4):
            for y in range(4):
                if x > 1 and y > 1:
                    self.assertGreater(self.coordinate, Coordinate(x, y), f"The coordinates ({x}, {y}) should be greater than (1, 1)")
                else:
                    self.assertFalse(self.coordinate > Coordinate(x, y), f"The coordinates ({x}, {y}) should not be greater than (1, 1)")
    
    def test_ge(self):
        for x in range(4):
            for y in range(4):
                if x >= 1 and y >= 1:
                    self.assertGreaterEqual(self.coordinate, Coordinate(x, y), f"The coordinates ({x}, {y}) should be greater than or equal to (1, 1)")
                else:
                    self.assertFalse(self.coordinate >= Coordinate(x, y), f"The coordinates ({x}, {y}) should not be greater than or equal to (1, 1)")
    
    def test_add(self):
        self.assertEqual(self.coordinate + Coordinate(2, 2), Coordinate(3, 3), "The coordinates should be added")
        with self.assertRaises(TypeError):
            self.coordinate + 1
    
    def test_sub(self):
        self.assertEqual(self.coordinate - Coordinate(2, 2), Coordinate(-1, -1), "The coordinates should be subtracted")
        with self.assertRaises(TypeError):
            self.coordinate - 1
    
    def test_mul(self):
        self.assertEqual(self.coordinate * Coordinate(2, 2), Coordinate(2, 2), "The coordinates should be multiplied")
        with self.assertRaises(TypeError):
            self.coordinate * 1

    def test_true_div(self):
        self.assertEqual(self.coordinate / Coordinate(2, 2), Coordinate(0.5, 0.5), "The coordinates should be divided")
        with self.assertRaises(TypeError):
            self.coordinate / 1
    
    def test_floordiv(self):
        self.assertEqual(self.coordinate // Coordinate(2, 2), Coordinate(0, 0), "The coordinates should be divided")
        with self.assertRaises(TypeError):
            self.coordinate // 1
    
    def test_mod(self):
        self.assertEqual(self.coordinate % Coordinate(2, 2), Coordinate(1, 1), "The coordinates should be divided")
        with self.assertRaises(TypeError):
            self.coordinate % 1
        
    def test_pow(self):
        self.assertEqual(self.coordinate ** Coordinate(2, 2), Coordinate(1, 1), "The coordinates should be divided")
        with self.assertRaises(TypeError):
            self.coordinate ** 1
    
    def test_lshift(self):
        self.assertEqual(self.coordinate << Coordinate(2, 2), Coordinate(4, 4), "The coordinates should be divided")
        with self.assertRaises(TypeError):
            self.coordinate << 1
    
    def test_rshift(self):
        self.assertEqual(self.coordinate >> Coordinate(2, 2), Coordinate(0, 0), "The coordinates should be divided")
        with self.assertRaises(TypeError):
            self.coordinate >> 1
    
    def test_and(self):
        self.assertEqual(self.coordinate & Coordinate(2, 2), Coordinate(0, 0), "The coordinates should be divided")
        with self.assertRaises(TypeError):
            self.coordinate & 1
    
    def test_xor(self):
        self.assertEqual(self.coordinate ^ Coordinate(2, 2), Coordinate(3, 3), "The coordinates should be divided")
        with self.assertRaises(TypeError):
            self.coordinate ^ 1
    
    def test_or(self):
        self.assertEqual(self.coordinate | Coordinate(2, 2), Coordinate(3, 3), "The coordinates should be divided")
        with self.assertRaises(TypeError):
            self.coordinate | 1
    
    def test_neg(self):
        self.assertEqual(-self.coordinate, Coordinate(-1, -1), "The coordinates should be negated")
    
    def test_pos(self):
        self.assertEqual(+self.coordinate, Coordinate(1, 1), "The coordinates should be positive")
    
    def test_abs(self):
        self.assertEqual(abs(self.coordinate), Coordinate(1, 1), "The coordinates should be positive")
    
    def test_invert(self):
        self.assertEqual(~self.coordinate, Coordinate(-2, -2), "The coordinates should be inverted")
    
    def test_str(self):
        self.assertEqual(str(self.coordinate), "(1, 1)", "The string should be equal to (1, 1)")
    
    def test_repr(self):
        self.assertEqual(repr(self.coordinate), "Coordinate(1, 1)", "The string should be equal to Coordinate(1, 1)")
        
if __name__ == '__main__':
    unittest.main()