import unittest
import main as m

class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.part_one = m.PartOne('test_one.txt')

    def test_two_full(self):
        self.test_two = m.PartOne('test_two.txt')
        self.assertEqual(self.test_two.total_winnings, 6592)

    def test_convert_cards_to_numbers(self):
        cards_to_nums = [
            [3, 2, 10, 3, 13, 765],
            [10, 5, 5, 11, 5, 684],
            [13, 13, 6, 7, 7, 28],
            [13, 10, 11, 11, 10, 220],
            [12, 12, 12, 11, 14, 483]
        ]
        actual = self.part_one.convert_cards_to_numbers()
        self.assertEqual(actual, cards_to_nums)

    def test_store_hand_types(self):
        self.assertEqual(len(self.part_one.high_card), 0)
        self.assertEqual(len(self.part_one.one_pair), 1)
        self.assertEqual(len(self.part_one.two_pair), 2)
        self.assertEqual(len(self.part_one.three_kind), 2)
        self.assertEqual(len(self.part_one.full_house), 0)
        self.assertEqual(len(self.part_one.four_kind), 0)
        self.assertEqual(len(self.part_one.five_kind), 0)

    def test_get_hand_type(self):
        high_card = self.part_one.get_hand_type([13, 2, 3, 4, 5])
        self.assertEqual(high_card, 'HighCard')

        one_pair = self.part_one.get_hand_type([13, 2, 13, 4, 5])
        self.assertEqual(one_pair, 'OnePair')

        two_pair = self.part_one.get_hand_type('AA556')
        self.assertEqual(two_pair, 'TwoPair')

        three_kind = self.part_one.get_hand_type('AAATK')
        self.assertEqual(three_kind, 'ThreeOfAKind')

        full_house = self.part_one.get_hand_type('ATAAT')
        self.assertEqual(full_house, 'FullHouse')

        four_kind = self.part_one.get_hand_type('AAATA')
        self.assertEqual(four_kind, 'FourOfAKind')

        five_kind = self.part_one.get_hand_type('AAAAA')
        self.assertEqual(five_kind, 'FiveOfAKind')

    def test_get_total_winnings(self):
        self.assertEqual(self.part_one.total_winnings, 6440)

    def test_organize_hands(self):
        self.assertEqual(self.part_one.two_pair,
            [[13, 10, 11, 11, 10, 220], [13, 13, 6, 7, 7, 28]]
        )
        self.assertEqual(self.part_one.three_kind,
            [[10, 5, 5, 11, 5, 684], [12, 12, 12, 11, 14, 483]]
        )

class TestPartTwo(unittest.TestCase):
    def setUp(self):
        self.part_two = m.PartTwo('test_two.txt')

    def test_get_total_winnings(self):
        self.assertEqual(self.part_two.total_winnings, 6839)

    def test_get_hand_type(self):
        high_card = self.part_two.get_hand_type([13, 12, 11, 10, 9])
        self.assertEqual(high_card, 'HighCard')

        one_pair = self.part_two.get_hand_type([13, 1, 2, 6, 5])
        self.assertEqual(one_pair, 'OnePair')

        two_pair = self.part_two.get_hand_type([13, 13, 5, 5, 6])
        self.assertEqual(two_pair, 'TwoPair')

        three_kind = self.part_two.get_hand_type([13, 13, 1, 10, 12])
        self.assertEqual(three_kind, 'ThreeOfAKind')

        full_house = self.part_two.get_hand_type([13, 10, 1, 10, 13])
        self.assertEqual(full_house, 'FullHouse')

        four_kind = self.part_two.get_hand_type([2, 2, 1, 10, 2])
        self.assertEqual(four_kind, 'FourOfAKind')

        five_kind = self.part_two.get_hand_type([2, 2, 2, 2, 1])
        self.assertEqual(five_kind, 'FiveOfAKind')
