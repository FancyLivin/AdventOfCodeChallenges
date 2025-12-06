def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().splitlines()

class ParabolicReflectorDish:
    def __init__(self, file_name) -> None:
        self.rock_map = read_file(file_name)
        self.rotated_map = [list(column) for column in zip(*self.rock_map)]
    
    def get_total_load(self) -> int:
        sum = 0
        self.iterate_through_rock_columns()
        self.rock_map = [list(column) for column in zip(*self.rotated_map)]

        for index, row in enumerate(self.rock_map):
            sum += row.count('O') * (len(self.rock_map)-index)
        return sum

    def iterate_through_rock_columns(self) -> None:
        for index, column in enumerate(self.rotated_map):
            self.rotated_map[index] = self.move_rocks(column)

    def move_rocks(self, column) -> list:
        round_rocks = 0
        square_rock = 0
        for index, value in enumerate(column):
            if value == 'O':
                round_rocks+=1
            if value == '#' or index == len(column)-1:
                for i in range(square_rock, index+1):
                    if column[i] == '#':
                        continue
                    elif round_rocks > 0:
                        round_rocks-=1
                        column[i] = 'O'
                    else:
                        column[i] = '.'
                square_rock = index+1
        return column

# one = ParabolicReflectorDish('real.txt')
# print('Part One:', one.get_total_load())