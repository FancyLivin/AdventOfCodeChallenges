def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

def create_difference_pyramid(line) -> list:
    extrapolated = [[int(num) for num in (line.rstrip('\n').split())]]
    while any(num != 0 for num in extrapolated[-1]):
        mini_list = []
        for index in range(len(extrapolated[-1]) - 1):
            num_one = extrapolated[-1][index]
            num_two = extrapolated[-1][index + 1]
            difference = num_two - num_one
            mini_list.append(difference)
        extrapolated.append(mini_list)
    return extrapolated

class PartOne:
    def __init__(self, file_name) -> None:
        self.input = read_file(file_name)
        self.sum = self.get_sum()

    def get_sum(self):
        sum = 0
        for line in self.input:
            pyramid = create_difference_pyramid(line)
            sum += self.get_next_value_prediction(pyramid)
        return sum
    
    def get_next_value_prediction(self, pyramid) -> int:
        curr_val = 0
        prev_val = 0
        prediction = 0

        for index in range(len(pyramid)-1, -1, -1):
            curr_val = pyramid[index][-1]
            prediction = curr_val + prev_val
            prev_val = prediction
        return prediction

class PartTwo:
    def __init__(self, file_name) -> None:
        self.input = read_file(file_name)
        self.sum = self.get_sum()

    def get_sum(self):
        sum = 0
        for line in self.input:
            pyramid = create_difference_pyramid(line)
            sum += self.get_prev_value_prediction(pyramid)
        return sum

    def get_prev_value_prediction(self, pyramid) -> int:
        curr_val = 0
        prev_val = 0
        prediction = 0

        for index in range(len(pyramid)-1, -1, -1):
            curr_val = pyramid[index][0]
            prediction = curr_val - prev_val
            prev_val = prediction
        return prediction

p_one = PartOne('real.txt')
print('Part One:', p_one.sum)

p_two = PartTwo('real.txt')
print('Part Two:', p_two.sum)