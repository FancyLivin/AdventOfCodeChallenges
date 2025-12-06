import unittest
import part_one as po
import part_two as pt

class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.one = po.PartOne('test_one.txt')

    def test_get_start_coords(self):
        self.assertEqual(self.one.start, (1, 1))
    
    def test_get_farthest_point(self):
        farthest = self.one.get_farthest_point()
        self.assertEqual(farthest, 4)

        self.two = po.PartOne('test_two.txt')
        farthest = self.two.get_farthest_point()
        self.assertEqual(farthest, 8)

    def test_move(self):
       current = self.one.move((1,1))
       self.assertEqual(current, (1,2))

       current = self.one.move((1,2))
       self.assertEqual(current, (1,3))

       current = self.one.move((1,3))
       self.assertEqual(current, (2,3))

       current = self.one.move((2,3))
       self.assertEqual(current, (3,3))

       current = self.one.move((3,3))
       self.assertEqual(current, (3,2))

       current = self.one.move((3,2))
       self.assertEqual(current, (3,1))

       current = self.one.move((3,1))
       self.assertEqual(current, (2,1))

       current = self.one.move((2,1))
       self.assertEqual(current, (1,1))

# Need to calculate area with vertices not with every point
class TestPartTwo(unittest.TestCase):
    def setUp(self):
        self.two = pt.PartTwo('test_one.txt')
    
    def test_shoelace_formula(self):
        self.two.navigate_pipes()
        area = self.two.get_shoelace_formula()
        self.assertEqual(area, 4)

    def test_get_total_interior_points(self):
        self.two.navigate_pipes()
        area = self.two.get_shoelace_formula()
        interior_points = self.two.get_total_interior_points(area)
        self.assertEqual(interior_points, 1)
