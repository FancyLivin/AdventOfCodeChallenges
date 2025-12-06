def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

class PartOne:
    def __init__(self, txt_file) -> None:
        self.file = read_file(txt_file)
        self.point_sum = 0

    def get_point_sum(self) -> int:
        for single_card in self.file:
            self.point_sum += self.calculate_card_points(single_card)
        return self.point_sum

    def calculate_card_points(self, string) -> int:
        card_points = 0
        card_numbers = string.split(' | ')

        winning_numbers = self.get_winning_numbers(card_numbers[0])
        your_numbers = self.get_numbers_you_have(card_numbers[1])

        for num in your_numbers:
            if num in winning_numbers and card_points == 0:
                card_points = 1
            elif num in winning_numbers and card_points >= 1:
                card_points *= 2

        return card_points

    def get_winning_numbers(self, string) -> list:
        winning_numbers = string.split()
        winning_numbers.pop(0)
        winning_numbers.pop(0)
        return winning_numbers

    def get_numbers_you_have(self, string) -> list:
        return string.split()

class PartTwo:
    def __init__(self, txt_file) -> None:
        self.txt_file = txt_file
        self.file = read_file(txt_file)
        self.card_dict = {}
        self.card_total = 0

    def populate_card_dict(self) -> None:
        for current_card in range(len(self.file)):
            self.card_dict[current_card] = 1

    def get_card_total(self) -> int:
        self.update_card_dict()
        for _, copies in self.card_dict.items():
            self.card_total += copies
        return self.card_total

    def update_card_dict(self) -> None:
        for card_index, card in enumerate(self.file):
            card_wins = self.get_card_wins(card)
            for win in range(card_wins):
                card_dupes = self.card_dict[card_index]
                self.card_dict[card_index + win + 1] += (1 * card_dupes) 

    def get_card_wins(self, string) -> int:
        card_wins = 0
        card_numbers = string.split(' | ')
        nums = PartOne(self.txt_file)

        winning_numbers = nums.get_winning_numbers(card_numbers[0])
        your_numbers = nums.get_numbers_you_have(card_numbers[1])

        for number in your_numbers:
            if number in winning_numbers:
                card_wins += 1

        return card_wins

part_one = PartOne('real_input.txt')
sum_one = part_one.get_point_sum()

part_two = PartTwo('real_input.txt')
part_two.populate_card_dict()
total_two = part_two.get_card_total()

print('Part One:', sum_one)
print('Part Two:', total_two)
