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

class PartOne:
    def __init__(self, file_name):
        self.p_map = read_file(file_name)
        self.start = get_start_coords(self.p_map)
    
    def get_farthest_point(self) -> int:
        farthest = 1
        current = self.move(self.start)
        while self.p_map[current[0]][current[1]] != 'S':
            current = self.move(current)
            farthest += 1
        return farthest // 2
    
    def move(self, current) -> tuple:
        x = current[0]
        y = current[1]
        current_pipe = self.store_coords(x, y)
        top = self.store_coords(x-1, y)
        right = self.store_coords(x, y+1)
        left = self.store_coords(x, y-1)
        bottom = self.store_coords(x+1, y)

        self.delete_pipe(current)
        if 'S' in pipe_map[top] and 'N' in pipe_map[current_pipe]:
            current = (x - 1, y)
        elif 'W' in pipe_map[right] and 'E' in pipe_map[current_pipe]:
            current = (x, y + 1)
        elif 'E' in pipe_map[left] and 'W' in pipe_map[current_pipe]:
            current = (x, y - 1)
        elif 'N' in pipe_map[bottom] and 'S' in pipe_map[current_pipe]:
            current = (x + 1, y)
        else:
            pass
        return current
    
    def store_coords(self, x, y):
        try:
            return self.p_map[x][y]
        except:
            return '.' 
    
    def delete_pipe(self, current):
        x = current[0]
        y = current[1]
        pipe = self.p_map[x][y]
        if pipe == 'S':
            return
        self.p_map[x] = self.p_map[x][:y] + '.' + self.p_map[x][y + 1:]

one = PartOne('real.txt')
print('Part One:', one.get_farthest_point())
