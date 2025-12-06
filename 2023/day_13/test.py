import unittest
import main as m

class TestPartOne(unittest.TestCase):
    def setUp(self) -> None:
        self.one = m.PointOfIncidence('test_one.txt')
        return

    def test_get_sum(self):
        sum = self.one.get_sum(False)
        return self.assertEqual(sum, 405)

    def test_get_pattern_score(self):
        test = [['#','.','#','#','.','.','#','#','.'],
                ['.','.','#','.','#','#','.','#','.'],
                ['#','#','.','.','.','.','.','.','#'],
                ['#','#','.','.','.','.','.','.','#'],
                ['.','.','#','.','#','#','.','#','.'],
                ['.','.','#','#','.','.','#','#','.'],
                ['#','.','#','.','#','#','.','#','.'],]
        i = self.one.get_pattern_score(test, False)
        return self.assertEqual(i, 5)

    def test_get_column_reflection_index(self):
        test = [['#','.','#','#','.','.','#','#','.'],
                ['.','.','#','.','#','#','.','#','.'],
                ['#','#','.','.','.','.','.','.','#'],
                ['#','#','.','.','.','.','.','.','#'],
                ['.','.','#','.','#','#','.','#','.'],
                ['.','.','#','#','.','.','#','#','.'],
                ['#','.','#','.','#','#','.','#','.'],]
        i = self.one.get_column_reflection_index(test, False)
        return self.assertEqual(i, 5)

    def test_get_row_reflection_index(self):
        test = [['#','.','.','.','#','#','.','.','#'],
                ['#','.','.','.','.','#','.','.','#'],
                ['.','.','#','#','.','.','#','#','#'],
                ['#','#','#','#','#','.','#','#','.'],
                ['#','#','#','#','#','.','#','#','.'],
                ['.','.','#','#','.','.','#','#','#'],
                ['#','.','.','.','.','#','.','.','#']]
        i = self.one.get_row_reflection_index(test, False)
        return self.assertEqual(i, 4)

class TestPartTwo(unittest.TestCase):
    def setUp(self) -> None:
        self.two = m.PointOfIncidence('test_one.txt')
        return
    
    def test_get_sum(self):
        sum = self.two.get_sum(True)
        return self.assertEqual(sum, 400)
