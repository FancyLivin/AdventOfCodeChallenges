# Part 1: 12 red cubes, 13 green cubes, 14 blue cubes maximum
def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

class PartOne:
    def __init__(self, txt_file) -> None:
        self.file = read_file(txt_file)
        self.id_sum = 0

    def get_id_sum(self) -> int:
        for full_game in self.file:
            add_to_sum = self.add_game_id_to_sum(full_game)
            self.id_sum += add_to_sum
        return self.id_sum

    def add_game_id_to_sum(self, string) -> int:
        split_string = string.split(';')
        for mini_game in split_string:
            if self.is_valid_game(mini_game) == False:
                return 0
        return self.get_game_id(string)

    def get_game_id(self, string) -> int:
        id_index = 5
        game_id = ''
        while (string[id_index] != ':'):
            game_id += string[id_index]
            id_index += 1
        return int(game_id)

    def is_valid_game(self, string) -> bool:
        max_red_cubes = 12
        max_green_cubes = 13
        max_blue_cubes = 14

        red_total = self.get_cube_total(string, 'red')
        green_total = self.get_cube_total(string, 'green')
        blue_total = self.get_cube_total(string, 'blue')

        if (red_total > max_red_cubes or
            green_total > max_green_cubes or
            blue_total > max_blue_cubes):
            return False
        return True

    def get_cube_total(self, string, cube_color) -> int:
        num_offset = 1
        no_cubes = 0

        split_string = string.replace(',', '')
        split_string = split_string.replace('\n', '')
        split_string = split_string.split(' ')

        try:
            index = split_string.index(cube_color)
            return int(split_string[index - num_offset])
        except:
            return no_cubes

class PartTwo:
    def __init__(self, txt_file) -> None:
        self.txt_file = txt_file
        self.file = read_file(txt_file)
        self.power_sum = 0

    def get_power_sum(self) -> int:
        for full_game in self.file:
            add_to_sum = self.get_cube_power(full_game)
            self.power_sum += add_to_sum
        return self.power_sum

    def get_cube_power(self, string) -> int:
        max_red_cubes = self.get_max_cube_count(string, 'red')
        max_green_cubes = self.get_max_cube_count(string, 'green')
        max_blue_cubes = self.get_max_cube_count(string, 'blue')

        return max_red_cubes * max_green_cubes * max_blue_cubes

    def get_max_cube_count(self, string, cube_color) -> int:
        max_cubes = 0
        cubes = PartOne(self.txt_file)

        split_string = string.split(';')
        for mini_game in split_string:
            current_cubes = cubes.get_cube_total(mini_game, cube_color)
            if current_cubes > max_cubes:
                max_cubes = current_cubes
        return max_cubes

part_one = PartOne('real_input.txt')
answer_one = part_one.get_id_sum()

part_two = PartTwo('real_input.txt')
answer_two = part_two.get_power_sum()

print(answer_one)
print(answer_two)