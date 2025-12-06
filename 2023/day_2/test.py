import unittest
import main as m

class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.part_one = m.PartOne('test_input.txt')

    def test_get_full_id_sum(self):
        sum = self.part_one.get_id_sum()

        self.assertEqual(sum, 8)

    def test_add_to_id_sum(self):
        game_one = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
        game_two = 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'

        get_one = self.part_one.add_game_id_to_sum(game_one)
        get_zero = self.part_one.add_game_id_to_sum(game_two)

        self.assertEqual(get_one, 1)
        self.assertEqual(get_zero, 0)

    def test_valid_game(self):
        game_one = self.part_one.is_valid_game('3 blue, 4 red')
        game_two = self.part_one.is_valid_game('8 green, 6 blue, 20 red')
        game_three = self.part_one.is_valid_game('3 green, 15 blue, 14 red')

        self.assertTrue(game_one)
        self.assertFalse(game_two)
        self.assertFalse(game_three)

    def test_get_game_id(self):
        test_three = 'Game 3: 8 green, 6 blue, 20 red'
        test_ninety = 'Game 90: 1 red, 13 green'

        id_three = self.part_one.get_game_id(test_three)
        id_ninety = self.part_one.get_game_id(test_ninety)

        self.assertEqual(id_three, 3)
        self.assertEqual(id_ninety, 90)

    def test_get_cubes(self):
        red_cubes = self.part_one.get_cube_total('3 blue, 4 red', 'red')
        green_cubes = self.part_one.get_cube_total('3 blue, 4 red', 'green')
        blue_cubes = self.part_one.get_cube_total('3 blue, 4 red', 'blue')
        
        self.assertEqual(red_cubes, 4)
        self.assertEqual(green_cubes, 0)
        self.assertEqual(blue_cubes, 3)

class TestPartTwo(unittest.TestCase):
    def setUp(self):
        self.part_two = m.PartTwo('test_input.txt')

    def test_get_power_sum(self):
        sum = self.part_two.get_power_sum()

        self.assertEqual(sum, 2286)

    def test_get_maximum_cube_count(self):
        game_three = 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'
        max_red_cubes = self.part_two.get_max_cube_count(game_three, 'red')
        max_green_cubes = self.part_two.get_max_cube_count(game_three, 'green')
        max_blue_cubes = self.part_two.get_max_cube_count(game_three, 'blue')

        self.assertEqual(max_red_cubes, 20)
        self.assertEqual(max_green_cubes, 13)
        self.assertEqual(max_blue_cubes, 6)

    def test_get_cube_power(self):
        game_three = 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'
        cube_power = self.part_two.get_cube_power(game_three)
        
        self.assertEqual(cube_power, 1560)
