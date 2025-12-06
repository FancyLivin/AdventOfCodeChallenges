def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

number_map = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
}

class PartOne:
    def __init__(self, txt_file) -> None:
        self.file = read_file(txt_file)
        self.sum = 0

    def calculate_sum_of_strings(self) -> None:
        for string in self.file:            
            first_num = self.get_first_number(string)
            last_num = self.get_last_number(string)
            combined_num = str(first_num) + str(last_num)
            self.sum += int(combined_num)

    def get_first_number(self, string) -> int:
        first_num = None
        for char in string:
            try:
                first_num = int(char)
                break
            except:
                continue
        return first_num

    def get_last_number(self, string) -> int:
        last_num = None
        for char in string:
            try:
                last_num = int(char)
            except:
                continue
        return last_num

class PartTwo:
    def __init__(self, txt_file) -> None:
        self.txt_name = txt_file
        self.file = read_file(txt_file)
        self.sum = 0

    def calculate_sum_of_strings(self) -> None:
        for string in self.file:
            updated_string = self.convert_str_to_num(string)

            get_nums = PartOne(self.txt_name)
            first_num = get_nums.get_first_number(updated_string)
            last_num = get_nums.get_last_number(updated_string)

            combined_num = str(first_num) + str(last_num)
            self.sum += int(combined_num)

    def convert_str_to_num(self, string) -> str:
        for word, number in number_map.items():
            string = string.replace(word, number)
        return string
