import unittest
import main as m

class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.part_one = m.PartOne('test_input_one.txt')
        self.part_one.store_conversion_maps()

    def test_get_seeds(self):
        seed_list = [79, 14, 55, 13]
        self.assertEqual(self.part_one.seeds, seed_list)

    def test_find_lowest_location(self):
        lowest_location = self.part_one.find_lowest_location()
        self.assertEqual(lowest_location, 35)

    def test_convert_seed_to_location(self):
        location = self.part_one.convert_seed_to_location(79)
        self.assertEqual(location, 82)

    def test_turn_seed_to_soil(self):
        soil_one = self.part_one.one_to_one_conversion(79, 'seed', 'soil')
        soil_two = self.part_one.one_to_one_conversion(14, 'seed', 'soil')
        soil_three = self.part_one.one_to_one_conversion(98, 'seed', 'soil')

        self.assertEqual(soil_one, 81)
        self.assertEqual(soil_two, 14)
        self.assertEqual(soil_three, 50)

    def test_turn_water_to_light(self):
        light = self.part_one.one_to_one_conversion(81, 'water', 'light')
        self.assertEqual(light, 74)

    def test_map_conversion_seed_soil(self):
        seed_soil_map = [[50, 98, 2], [52, 50, 48]]
        map = self.part_one.map_conversion(2)
        self.assertEqual(map, seed_soil_map)

    def test_map_conversion_humid_loc(self):
        humid_loc_map = [[60, 56, 37], [56, 93, 4]]
        map = self.part_one.map_conversion(30)
        self.assertEqual(map, humid_loc_map)

class TestPartTwo(unittest.TestCase):
    def setUp(self):
        self.part_two = m.PartTwo('test_input_one.txt')

    def test_find_lowest_location(self):
        self.part_two.find_lowest_location()
        self.assertEqual(self.part_two.lowest_location, 46)
