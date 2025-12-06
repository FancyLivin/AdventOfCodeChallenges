# dest source range

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

class PartOne:
    def __init__(self, file_name) -> None:
        self.input = read_file(file_name)
        self.seeds = self.get_seeds()
        self.lowest_location = float('inf')

        self.seed_soil_map = None
        self.soil_fert_map = None
        self.fert_water_map = None
        self.water_light_map = None
        self.light_temp_map = None
        self.temp_humid_map = None
        self.humid_loc_map = None

    def get_seeds(self) -> list:
        seed_list = self.input[0].strip('seeds: ').split()
        return [eval(seed) for seed in seed_list]
    
    def find_lowest_location(self) -> int:
        for seed in self.seeds:
            current_location = self.convert_seed_to_location(seed)
            if current_location < self.lowest_location:
                self.lowest_location = current_location
        return self.lowest_location

    def convert_seed_to_location(self, seed) -> int:
        soil = self.one_to_one_conversion(seed, 'seed', 'soil')
        fert = self.one_to_one_conversion(soil, 'soil', 'fert')
        water = self.one_to_one_conversion(fert, 'fert', 'water')
        light = self.one_to_one_conversion(water, 'water', 'light')
        temp = self.one_to_one_conversion(light, 'light', 'temp')
        humid = self.one_to_one_conversion(temp, 'temp', 'humid')
        location = self.one_to_one_conversion(humid, 'humid', 'loc')
        return location

    def one_to_one_conversion(self, source_val, source_type, dest_type) -> int:
        dest_val = source_val
        map_name = f'{source_type}_{dest_type}_map'
        map_list = getattr(self, map_name)

        for dest_start, src_start, range_len in map_list:
            if source_val >= src_start and source_val < src_start + range_len:
                return source_val - (src_start - dest_start)
        return dest_val

    def store_conversion_maps(self) -> None:
        for index in range(len(self.input)):
            if self.input[index] == 'seed-to-soil map:\n':
                self.seed_soil_map = self.map_conversion(index)
            if self.input[index] == 'soil-to-fertilizer map:\n':
                self.soil_fert_map = self.map_conversion(index)
            if self.input[index] == 'fertilizer-to-water map:\n':
                self.fert_water_map = self.map_conversion(index)
            if self.input[index] == 'water-to-light map:\n':
                self.water_light_map = self.map_conversion(index)
            if self.input[index] == 'light-to-temperature map:\n':
                self.light_temp_map = self.map_conversion(index)
            if self.input[index] == 'temperature-to-humidity map:\n':
                self.temp_humid_map = self.map_conversion(index)
            if self.input[index] == 'humidity-to-location map:\n':
                self.humid_loc_map = self.map_conversion(index)

    def map_conversion(self, index) -> list:
        map = []
        for _ in self.input:
            index += 1
            if self.is_new_line(index):
                break
            line = self.input[index].split()
            map.append([eval(num) for num in line])
            if self.is_end_of_file(index):
                break
        return map
    
    def is_new_line(self, index) -> bool:
        if self.input[index] == '\n':
            return True
        return False
    
    def is_end_of_file(self, index) -> bool:
        if index == len(self.input) - 1:
            return True
        return False

class PartTwo:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.input = read_file(file_name)
        self.big_counter = 0
        self.seeds = []
        self.lowest_location = float('inf')

    def find_lowest_location(self) -> int:
        part_one = PartOne(self.file_name)
        part_one.store_conversion_maps()
        for start, length in zip(part_one.seeds[::2], part_one.seeds[1::2]):
            for seed in range(start, start + length):
                self.big_counter += 1
                if self.big_counter % 10000000 == 0:
                    print(f"current number passed is {self.big_counter}")
                location = part_one.convert_seed_to_location(seed)
                if location < self.lowest_location:
                    self.lowest_location = location
        return self.lowest_location

part_one = PartOne('real_input.txt')
part_one.store_conversion_maps()
part_one.find_lowest_location()
print('Part One:', part_one.lowest_location)

part_two = PartTwo('real_input.txt')
part_two.find_lowest_location()
print('Part Two:', part_two.lowest_location)