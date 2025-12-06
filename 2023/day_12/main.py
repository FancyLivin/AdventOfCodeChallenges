from itertools import combinations


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().splitlines()

class HotSprings:
    def __init__(self, file_name):
        self.hot_springs = read_file(file_name)

    def find_possible_arrangements(self, hot_spring) -> int:
        spring_list, arrangement = hot_spring.split()
        spring_list = spring_list.strip('.').rstrip('.')
        arrangement = [int(x) for x in arrangement.split(',')]

        if sum(arrangement) + len(arrangement)-1 == len(spring_list):
            return 1
        
        
        print(spring_list)

        return 0

    def split_string(self, hot_spring) -> (str, str):
        return hot_spring.split()
