import unittest
import main as m

class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.one = m.PartOne('test_one.txt')

    def test_get_sum(self):
        self.assertEqual(self.one.sum, 114)
    
    def test_create_pyramid(self):
        test = [[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0, 0, 0, 0]]
        pyramid = m.create_difference_pyramid('0 3 6 9 12 15\n')
        self.assertEqual(pyramid, test)

    def test_get_next_value(self):
        pyramid = m.create_difference_pyramid('0 3 6 9 12 15\n')
        next_val = self.one.get_next_value_prediction(pyramid)
        self.assertEqual(next_val, 18)

        pyramid = m.create_difference_pyramid('1 3 6 10 15 21\n')
        next_val = self.one.get_next_value_prediction(pyramid)
        self.assertEqual(next_val, 28)

        pyramid = m.create_difference_pyramid('10 13 16 21 30 45\n')
        next_val = self.one.get_next_value_prediction(pyramid)
        self.assertEqual(next_val, 68)

class TestPartTwo(unittest.TestCase):
    def setUp(self) -> None:
        self.two = m.PartTwo('test_one.txt')

    def test_get_sum(self):
        self.assertEqual(self.two.sum, 2)
    
    def test_get_prev_value(self):
        pyramid = m.create_difference_pyramid('10 13 16 21 30 45\n')
        prev_val = self.two.get_prev_value_prediction(pyramid)
        self.assertEqual(prev_val, 5)
