import unittest
import main as m

class TestPartOne(unittest.TestCase):
    def setUp(self) -> None:
        self.one = m.ParabolicReflectorDish('test_one.txt')
    
    def test_get_total_load(self):
        total = self.one.get_total_load()
        return self.assertEqual(total, 136)

    def test_iterate_through_rock_columns(self):
        expected = [
            ['O', 'O', 'O', 'O', '.', '.', '.', '.', '#', '#'],
            ['O', 'O', 'O', '.', '.', '.', '.', '.', '.', '.'],
            ['O', '.', '.', '.', '.', '#', 'O', 'O', '.', '.'],
            ['O', '.', '.', '#', '.', '.', '.', '.', '.', '.'],
            ['.', '#', 'O', '.', '.', '.', '.', '.', '.', '.'],
            ['#', '.', '#', 'O', '.', '.', '#', '.', '#', '#'],
            ['.', '.', '#', 'O', '.', '.', '.', '.', '#', '.'],
            ['O', '.', '.', '.', '.', '#', 'O', '.', '#', '.'],
            ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
            ['.', '#', 'O', '.', '.', '#', 'O', '.', '.', '.']
        ]
        self.one.iterate_through_rock_columns()
        return self.assertEqual(expected, self.one.rotated_map)

    def test_move_rocks1(self):
        test = ['O', '.', 'O', 'O', '#', '.', '.', '.', '.', '#']
        expected = ['O', 'O', 'O', '.', '#', '.', '.', '.', '.', '#']
        column = self.one.move_rocks(test)
        return self.assertEqual(column, expected)
    
    def test_move_rocks2(self):
        test = ['O', 'O', '.', '#', 'O', '.', '.', '.', '.', 'O']
        expected = ['O', 'O', '.', '#', 'O', 'O', '.', '.', '.', '.']
        column = self.one.move_rocks(test)
        return self.assertEqual(column, expected)

class TestPartTwo(unittest.TestCase):
    def setUp(self) -> None:
        self.two = m.ParabolicReflectorDish('test_one.txt')
