def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().splitlines()

class CosmicExpansion:
    def __init__(self, text_file) -> None:
        self.universe = read_file(text_file)

    def get_minimum_travel_sum(self, expansion_rate) -> int:
        sum = 0
        universe = self.expand_universe(self.universe)
        galaxy_list = self.get_galaxy_indicies(universe, expansion_rate)
        for x, galaxy_one in enumerate(galaxy_list):
            for y, galaxy_two in enumerate(galaxy_list):
                if y > x:
                    sum += self.get_minimum_travel_steps(galaxy_one, galaxy_two)
        return sum
    
    # expanded (up-down is |, left-right is -, all directions is +) 
    def expand_universe(self, universe) -> list:
        expanded_universe = self.expand_columns(universe)
        expanded_universe = self.expand_rows(expanded_universe)
        return expanded_universe
    
    def expand_columns(self, universe) -> list:
        for y in range(len(universe)-1, 0, -1):
            column = ''
            for x in range(len(universe)):
                column += universe[x][y]
            if '#' not in column:
                for i in range(len(universe)):
                    universe[i] = universe[i][:y] + '-' + universe[i][y+1:]
        return universe

    def expand_rows(self, universe) -> list:
        for i, row in enumerate(universe):
            if '#' not in row:
                universe[i] = (universe[i].replace('-','+').replace('.','|'))
        return universe
    
    def get_galaxy_indicies(self, universe, expansion_rate) -> list:
        galaxies = []
        expanded_x = 0
        for x in range(len(universe)):
            expanded_y = 0
            if '|' in universe[x]:
                expanded_x+=expansion_rate
            for y in range(len(universe[0])):
                if universe[x][y] in ['-', '+']:
                    expanded_y+=expansion_rate
                if universe[x][y] == '#':
                    galaxies.append((expanded_x,expanded_y))
                expanded_y+=1
            expanded_x+=1
        return galaxies

    # distance calculated using manhattan distance formula
    def get_minimum_travel_steps(self, p, q) -> int:
        return abs(p[0] - q[0]) + abs(p[1] - q[1])

cosmic = CosmicExpansion('real.txt')
print('Part One:', cosmic.get_minimum_travel_sum(1))
print('Part Two:', cosmic.get_minimum_travel_sum(999999))
