import unittest
import main as m

class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.part_one = m.PartOne('real_input.txt')

    def test_calculate_sum(self):
        real_int = 56049
        test_int = 142

        test = m.PartOne('test_input_one.txt')
        test.calculate_sum_of_strings()
        self.part_one.calculate_sum_of_strings()

        self.assertEqual(self.part_one.sum, real_int)
        self.assertEqual(test.sum, test_int)

    def test_get_first_number(self):
        one = self.part_one.get_first_number('a1b2c3d4e5f')
        three = self.part_one.get_first_number('pqr3stu8vwx')

        self.assertEqual(one, 1)
        self.assertEqual(three, 3)

    def test_get_last_number(self):
        two = self.part_one.get_last_number('1abc2')
        seven = self.part_one.get_last_number('treb7uchet')

        self.assertEqual(seven, 7)
        self.assertEqual(two, 2)

class TestPartTwo(unittest.TestCase):
    def setUp(self):
        self.part_two = m.PartTwo('real_input.txt')

    def test_convert_string_to_number(self):
        new_string = self.part_two.convert_str_to_num('two1nine')
        shared_num_string = self.part_two.convert_str_to_num('eightwothree')

        self.assertEqual(shared_num_string, 'e8t2ot3e')
        self.assertEqual(new_string, 't2o1n9e')

    def test_calculate_sum_of_strings(self):
        test = m.PartTwo('test_input_two.txt')
        test.calculate_sum_of_strings()
        self.part_two.calculate_sum_of_strings()

        self.assertEqual(test.sum, 281)
        self.assertEqual(self.part_two.sum, 54530)
