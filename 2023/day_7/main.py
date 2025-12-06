from collections import Counter

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

card_map = {
    'A': 14, 'K': 13, 'Q': 12, 'J': 11,
    'T': 10, '9': 9, '8': 8, '7': 7,
    '6': 6, '5': 5, '4': 4, '3': 3,
    '2': 2
}
joker_map = {
    'A': 13, 'K': 12, 'Q': 11, 'T': 10, 
    '9': 9, '8': 8, '7': 7, '6': 6,
    '5': 5, '4': 4, '3': 3, '2': 2,
    'J': 1
}

class PartOne:
    def __init__(self, file_name) -> None:
        self.input = read_file(file_name)
        self.cards_to_nums = self.convert_cards_to_numbers()

        self.high_card = []
        self.one_pair = []
        self.two_pair = []
        self.three_kind = []
        self.full_house = []
        self.four_kind = []
        self.five_kind = []

        self.total_winnings = self.store_total_winnings()

    def convert_cards_to_numbers(self) -> list:
        cards_to_nums = []
        for line in self.input:
            hand = []
            for card in line.split().pop(0):
                hand.append(card_map[card])
            hand.append(int(line.split().pop(1)))
            cards_to_nums.append(hand)
        return cards_to_nums

    def store_hand_types(self) -> None:
        for line in self.cards_to_nums:
            hand = line[:5]
            hand_type = self.get_hand_type(hand)

            if hand_type == 'HighCard':
                self.high_card.append(line)
            if hand_type == 'OnePair':
                self.one_pair.append(line)
            if hand_type == 'TwoPair':
                self.two_pair.append(line)
            if hand_type == 'ThreeOfAKind':
                self.three_kind.append(line)
            if hand_type == 'FullHouse':
                self.full_house.append(line)
            if hand_type == 'FourOfAKind':
                self.four_kind.append(line)
            if hand_type == 'FiveOfAKind':
                self.five_kind.append(line)

    def get_hand_type(self, hand) -> str:
        card_occurences = sorted(Counter(hand).values(), reverse=True)
        if card_occurences[0] == 5:
            return 'FiveOfAKind'
        if card_occurences[0] == 4:
            return 'FourOfAKind'
        if card_occurences[0] == 3 and card_occurences[1] == 2:
            return 'FullHouse'
        if card_occurences[0] == 3:
            return 'ThreeOfAKind'
        if card_occurences[0] == 2 and card_occurences[1] == 2:
            return 'TwoPair'
        if card_occurences[0] == 2:
            return 'OnePair'
        return 'HighCard'
    
    def store_total_winnings(self) -> int:
        total_winnings = 0
        self.store_hand_types()

        self.organize_hands_descending(self.high_card)
        self.organize_hands_descending(self.one_pair)
        self.organize_hands_descending(self.two_pair)
        self.organize_hands_descending(self.three_kind)
        self.organize_hands_descending(self.full_house)
        self.organize_hands_descending(self.four_kind)
        self.organize_hands_descending(self.five_kind)

        hand_list = (self.high_card + self.one_pair +
                     self.two_pair + self.three_kind +
                     self.full_house + self.four_kind +
                     self.five_kind)
        hand_list = [arr[5] for arr in hand_list]

        for index, bet in enumerate(hand_list, 1):
            total_winnings += (bet * index)
        return total_winnings

    def organize_hands_descending(self, list) -> None:
        list.sort(reverse=False, key=self.get_hand_sum)
    
    def get_hand_sum(self, hand) -> int:
        return ((hand[0] * (13 ** 4)) + (hand[1] * (13 ** 3)) +
                (hand[2] * (13 ** 2)) + (hand[3] * 13) +
                hand[4])

class PartTwo:
    def __init__(self, file_name) -> None:
        self.input = read_file(file_name)
        self.cards_to_nums = self.convert_cards_to_numbers()

        self.high_card = []
        self.one_pair = []
        self.two_pair = []
        self.three_kind = []
        self.full_house = []
        self.four_kind = []
        self.five_kind = []

        self.total_winnings = self.store_total_winnings()

    def convert_cards_to_numbers(self) -> list:
        cards_to_nums = []
        for line in self.input:
            hand = []
            for card in line.split().pop(0):
                hand.append(joker_map[card])
            hand.append(int(line.split().pop(1)))
            cards_to_nums.append(hand)
        return cards_to_nums

    def store_hand_types(self) -> None:
        for line in self.cards_to_nums:
            hand = line[:5]
            hand_type = self.get_hand_type(hand)

            if hand_type == 'HighCard':
                self.high_card.append(line)
            if hand_type == 'OnePair':
                self.one_pair.append(line)
            if hand_type == 'TwoPair':
                self.two_pair.append(line)
            if hand_type == 'ThreeOfAKind':
                self.three_kind.append(line)
            if hand_type == 'FullHouse':
                self.full_house.append(line)
            if hand_type == 'FourOfAKind':
                self.four_kind.append(line)
            if hand_type == 'FiveOfAKind':
                self.five_kind.append(line)

    def get_hand_type(self, hand) -> int:
        jokers = hand.count(1)
        hand = [c for c in hand if c != 1]
        if len(hand) == 0:
            return 'FiveOfAKind'
        card_occurences = sorted(Counter(hand).values(), reverse=True)
        if card_occurences[0] + jokers == 5:
            return 'FiveOfAKind'
        if card_occurences[0] + jokers == 4:
            return 'FourOfAKind'
        if card_occurences[0] + jokers == 3 and card_occurences[1] == 2:
            return 'FullHouse'
        if card_occurences[0] + jokers == 3:
            return 'ThreeOfAKind'
        if card_occurences[0] == 2 and card_occurences[1] == 2:
            return 'TwoPair'
        if card_occurences[0] + jokers == 2:
            return 'OnePair'
        return 'HighCard'
    
    def store_total_winnings(self) -> int:
        total_winnings = 0
        self.store_hand_types()

        self.organize_hands_descending(self.high_card)
        self.organize_hands_descending(self.one_pair)
        self.organize_hands_descending(self.two_pair)
        self.organize_hands_descending(self.three_kind)
        self.organize_hands_descending(self.full_house)
        self.organize_hands_descending(self.four_kind)
        self.organize_hands_descending(self.five_kind)

        hand_list = (self.high_card + self.one_pair +
                     self.two_pair + self.three_kind +
                     self.full_house + self.four_kind +
                     self.five_kind)
        hand_list = [arr[5] for arr in hand_list]

        for index, bet in enumerate(hand_list, 1):
            total_winnings += (bet * index)
        return total_winnings

    def organize_hands_descending(self, list) -> None:
        list.sort(reverse=False, key=self.get_hand_sum)
    
    def get_hand_sum(self, hand) -> int:
        return ((hand[0] * (13 ** 4)) + (hand[1] * (13 ** 3)) +
                (hand[2] * (13 ** 2)) + (hand[3] * 13) +
                hand[4])

part_one = PartOne('real.txt')
print('Part One:', part_one.total_winnings)

part_two = PartTwo('real.txt')
print('Print Two:', part_two.total_winnings)