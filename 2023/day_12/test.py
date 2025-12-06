import unittest
from itertools import combinations
import main as m

class TestPartOne(unittest.TestCase):
    def setUp(self) -> None:
        self.one = m.HotSprings('test_one.txt')

    def test_find_one_arrangement(self):
        one_arrangement = self.one.find_possible_arrangements('???.### 1,1,3')
        self.assertEqual(one_arrangement, 1)

    def test_find_multiple_arrangements(self):
        multiple_arrangements = self.one.find_possible_arrangements('.??..??...?##. 1,1,3')
        self.assertEqual(multiple_arrangements, 4)

    def test_get_combinations(self):
        wow = m.solve('????.#...#...')
        print(wow)

class TestPartTwo(unittest.TestCase):
    pass
