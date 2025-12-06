import unittest
import main as m

class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.part_one = m.PartOne('test_input_one.txt')
        self.part_one.populate_engine_map()

    def test_populate_engine_map(self):
        map_length = len(self.part_one.engine_map)
        map_height = len(self.part_one.engine_map[0])

        self.assertEqual(map_length, 10)
        self.assertEqual(map_height, 10)

    def test_get_part_number_sum(self):
        sum = self.part_one.get_part_number_sum()

        self.assertEqual(sum, 4475)
    
    def test_is_symbol(self):
        valid_symbol = self.part_one.is_symbol('@')
        invalid_symbol = self.part_one.is_symbol(')')

        self.assertTrue(valid_symbol)
        self.assertFalse(invalid_symbol)
    
    def test_get_sum_around_symbol(self):
        full_search = self.part_one.get_sum_around_symbol(5, 8)
        partial_top_search = self.part_one.get_sum_around_symbol(4, 0)
        partial_left_search = self.part_one.get_sum_around_symbol(0, 5)
        partial_right_search = self.part_one.get_sum_around_symbol(9, 1)
        partial_bottom_search = self.part_one.get_sum_around_symbol(4, 9)
        
        self.assertEqual(full_search, 1353)
        self.assertEqual(partial_top_search, 114)
        self.assertEqual(partial_left_search, 617)
        self.assertEqual(partial_right_search, 633)
        self.assertEqual(partial_bottom_search, 664)

    def test_get_part_number(self):
        first_num = self.part_one.extract_part_number(2, 0)
        second_num = self.part_one.extract_part_number(5, 0)
        third_num = self.part_one.extract_part_number(7, 5)
        
        self.assertEqual(first_num, 467)
        self.assertEqual(second_num, 114)
        self.assertEqual(third_num, 581)
    
    def test_get_zero_from_part_number(self):
        first_symbol = self.part_one.extract_part_number(1, 6)
        second_symbol = self.part_one.extract_part_number(5, 6)

        self.assertEqual(first_symbol, 0)
        self.assertEqual(second_symbol, 0)

    def test_delete_part_number_one(self):
        self.part_one.delete_part_number(2, 0)

        self.assertEqual(self.part_one.engine_map[0], '....+114..')
    
    def test_delete_part_number_two(self):
        self.part_one.delete_part_number(5, 0)

        self.assertEqual(self.part_one.engine_map[0], '467.+.....')

    def test_delete_part_number_three(self):
        self.part_one.delete_part_number(7, 5)
        
        self.assertEqual(self.part_one.engine_map[5], '+....+....')

    def test_go_to_start_index(self):
        start_index_one = self.part_one.go_to_part_number_start_index(2, 0)
        start_index_two = self.part_one.go_to_part_number_start_index(5, 0)
        start_index_three = self.part_one.go_to_part_number_start_index(8, 5)

        self.assertEqual(start_index_one, 0)
        self.assertEqual(start_index_two, 5)
        self.assertEqual(start_index_three, 7)

class TestPartTwo(unittest.TestCase):
    def setUp(self):
        self.part_two = m.PartTwo('test_input_two.txt')
        self.part_two.populate_engine_map()

    def test_get_gear_ratio_sum(self):
        sum = self.part_two.get_gear_ratio_sum()

        self.assertEqual(sum, 1037860)
    
    def test_is_gear(self):
        valid_gear = self.part_two.is_gear('*')
        invalid_gear = self.part_two.is_gear('-')

        self.assertTrue(valid_gear)
        self.assertFalse(invalid_gear)

    def test_get_gear_ratio(self):
        zero = self.part_two.get_gear_ratio(3, 4)
        big_num_one = self.part_two.get_gear_ratio(3, 1)
        big_num_two = self.part_two.get_gear_ratio(7, 6)

        self.assertEqual(zero, 0)
        self.assertEqual(big_num_one, 16345)
        self.assertEqual(big_num_two, 570025)
    