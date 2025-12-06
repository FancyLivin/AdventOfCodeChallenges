def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

class PartOne:
    def __init__(self, file_name) -> None:
        self.input = read_file(file_name)
        self.races = self.store_races()
        self.record_beaters = 1

    def store_races(self) -> dict:
        dict = {}

        for line in self.input:
            total_races = line.split()
            total_races.pop(0)
            for index, value in enumerate(total_races):
                if 'Time' in line:
                    dict[f'race{index+1}'] = {}
                    dict[f'race{index+1}']['Time'] = int(value)
                else:
                    dict[f'race{index+1}']['Distance'] = int(value)

        return dict
    
    def get_total_record_beaters(self) -> int:
        for race, _ in self.races.items():
            self.record_beaters *= self.get_current_race_record(race)
        return self.record_beaters
    
    def get_current_race_record(self, race) -> int:
        possible_records = 0
        total_time = self.races[race]['Time']

        for time_held in range(total_time):
            if self.is_record_breaking(race, time_held):
                possible_records += 1
        return possible_records

    def is_record_breaking(self, race, time_held) -> bool:
        remaining_time = self.races[race]['Time'] - time_held
        distance_traveled = remaining_time * time_held
        record_distance = self.races[race]['Distance']

        if distance_traveled > record_distance:
            return True
        return False

class PartTwo:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.input = read_file(file_name)
        self.race = self.store_race()
        self.record_beaters = 0

    def store_race(self) -> dict:
        time = int(''.join(self.input[0].strip('Time:').split()))
        distance = int(''.join(self.input[1].strip('Distance:').split()))

        return {'race1': {'Time': time, 'Distance': distance}}
    
    def get_total_record_beaters(self) -> int:
        total_time = self.race['race1']['Time']

        for time_held in range(total_time):
            if self.is_record_breaking(time_held):
                self.record_beaters += 1
        return self.record_beaters

    def is_record_breaking(self, time_held) -> bool:
        remaining_time = self.race['race1']['Time'] - time_held
        distance_traveled = remaining_time * time_held
        record_distance = self.race['race1']['Distance']

        if distance_traveled > record_distance:
            return True
        return False

part_one = PartOne('real_input.txt')
total_records_one = part_one.get_total_record_beaters()

part_two = PartTwo('real_input.txt')
total_records_two = part_two.get_total_record_beaters()

print('Part One:', total_records_one)
print('Part Two:', total_records_two)