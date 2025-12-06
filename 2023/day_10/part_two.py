def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return [line.rstrip('\n') for line in lines]

pipe_map = {
    '|' : 'NS',
    '-' : 'EW',
    'L' : 'NE',
    'J' : 'NW',
    '7' : 'SW',
    'F' : 'SE',
    '.' : 'X',
    'P' : 'X',
    'S' : 'NSEW'
}

def get_start_coords(map) -> tuple:
    for x, row in enumerate(map):
        for y, point in enumerate(row):
            if point == 'S':
                return (x, y)
    return (-1, -1)

class PartTwo:
    def __init__(self, file_name):
        self.p_map = read_file(file_name)
        self.start = get_start_coords(self.p_map)
        self.coords = []
        self.vertices = []

    def get_shoelace_formula(self) -> float:
        area = 0
        for i, _ in enumerate(self.vertices):
            if i == len(self.vertices) - 1:
                break
            area += ((self.vertices[i][0]*self.vertices[i+1][1]) - (self.vertices[i+1][0]*self.vertices[i][1]))
        area += ((self.vertices[-1][0]*self.vertices[0][1]) - (self.vertices[0][0]*self.vertices[-1][1]))
        return abs(area // 2)
    
    def get_total_interior_points(self, area) -> int:
        return 1 + area - ((len(self.coords)) / 2)

    def navigate_pipes(self):
        current = self.move(self.start)
        while self.p_map[current[0]][current[1]] != 'S' and len(self.coords) > 0:
            current = self.move(current)
    
    def move(self, current) -> tuple:
        x = current[0]
        y = current[1]
        current_pipe = self.store_coords(x, y)
        top = self.store_coords(x-1, y)
        right = self.store_coords(x, y+1)
        left = self.store_coords(x, y-1)
        bottom = self.store_coords(x+1, y)

        self.coords.append((x,y))
        if current_pipe in ['F', '7', 'J', 'L', 'S']:
            self.vertices.append((x,y))
        if 'S' in pipe_map[top] and 'N' in pipe_map[current_pipe] and (x-1,y) not in self.coords:
            current = (x - 1, y)
        elif 'W' in pipe_map[right] and 'E' in pipe_map[current_pipe] and (x,y+1) not in self.coords:
            current = (x, y + 1)
        elif 'E' in pipe_map[left] and 'W' in pipe_map[current_pipe] and (x,y-1) not in self.coords:
            current = (x, y - 1)
        elif 'N' in pipe_map[bottom] and 'S' in pipe_map[current_pipe] and (x+1,y) not in self.coords:
            current = (x + 1, y)
        else:
            return self.start
        return current
    
    def store_coords(self, x, y):
        try:
            return self.p_map[x][y]
        except:
            return '.' 
    
    def convert_pipe_to_letter(self, current):
        x = current[0]
        y = current[1]
        pipe = self.p_map[x][y]
        if pipe == 'S':
            return
        self.p_map[x] = self.p_map[x][:y] + 'P' + self.p_map[x][y + 1:]

two = PartTwo('real.txt')
two.navigate_pipes()
area = two.get_shoelace_formula()
interior_points = two.get_total_interior_points(area)
print('Part Two:', interior_points)
