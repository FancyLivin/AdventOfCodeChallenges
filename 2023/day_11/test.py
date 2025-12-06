import unittest
import main as m

class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.one = m.CosmicExpansion('test_one.txt')
    
    def test_no_new_line(self):
        self.assertEqual(self.one.universe[0], '...#......')

    def test_get_minimum_sum(self):
        small_sum = self.one.get_minimum_travel_sum(1)
        self.assertEqual(small_sum, 374)

    def test_get_large_minimum_sum(self):
        big_sum = self.one.get_minimum_travel_sum(99)
        self.assertEqual(big_sum, 8410)

    def test_expand_universe(self):
        expanded_universe = self.one.expand_universe(self.one.universe)
        test_universe = [
            '..-#.-..-.',
            '..-..-.#-.',
            '#.-..-..-.',
            '||+||+||+|',
            '..-..-#.-.',
            '.#-..-..-.',
            '..-..-..-#',
            '||+||+||+|',
            '..-..-.#-.',
            '#.-.#-..-.'
        ]
        self.assertEqual(expanded_universe, test_universe)

    def test_expand_columns(self):
        expanded_columns = self.one.expand_columns(self.one.universe)
        test_universe = [
            '..-#.-..-.',
            '..-..-.#-.',
            '#.-..-..-.',
            '..-..-..-.',
            '..-..-#.-.',
            '.#-..-..-.',
            '..-..-..-#',
            '..-..-..-.',
            '..-..-.#-.',
            '#.-.#-..-.'
        ]
        self.assertEqual(expanded_columns, test_universe)

    def test_expand_rows(self):
        expanded_rows = self.one.expand_rows(self.one.universe)
        test_universe = [
            '...#......',
            '.......#..',
            '#.........',
            '||||||||||',
            '......#...',
            '.#........',
            '.........#',
            '||||||||||',
            '.......#..',
            '#...#.....'
        ]
        self.assertEqual(expanded_rows, test_universe)

    def test_find_total_galaxies(self):
        universe = self.one.expand_universe(self.one.universe)
        total_galaxies = self.one.get_galaxy_indicies(universe, 1)
        test_galaxies = [(0,4), (1,9), (2,0), (5,8), (6,1),
                         (7,12), (10,9), (11,0), (11,5)]
        self.assertEqual(total_galaxies, test_galaxies)

    def test_get_minimum_steps(self):
        distance = self.one.get_minimum_travel_steps((6,1), (11,5))
        self.assertEqual(distance, 9)
