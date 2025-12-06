def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().splitlines() + ['']

class PointOfIncidence:
    def __init__(self, file_name) -> None:
        self.patterns = read_file(file_name)

    def get_sum(self, is_p2) -> int:
        sum = 0
        pattern = []
        for line in self.patterns:
            if line == '':
                sum += self.get_pattern_score(pattern, is_p2)
                pattern.clear()
                continue
            pattern.append(list(line))
        return sum

    def get_pattern_score(self, pattern, is_p2) -> int:
        score = self.get_column_reflection_index(pattern, is_p2)
        score = score if score != 0 else 100*self.get_row_reflection_index(pattern, is_p2)
        return score

    def get_column_reflection_index(self, pattern, is_p2) -> int:
        columns = [list(column) for column in zip(*pattern)]
        for i, _ in enumerate(columns, 1):
            if i == len(columns):
                return 0
            if self.is_valid_reflection(columns, i, is_p2):
                return i

    def get_row_reflection_index(self, pattern, is_p2) -> int:
        for i, _ in enumerate(pattern, 1):
            if self.is_valid_reflection(pattern, i, is_p2):
                return i
            
    def is_valid_reflection(self, pattern, index, is_p2) -> bool:
        g = 0
        has_smudge = False
        while (index-1-g >= 0) and (index+g < len(pattern)):
            if pattern[index-1-g] != pattern[index+g]:
                if is_p2 and self.is_smudge(pattern[index-1-g], pattern[index+g]):
                    g+=1
                    has_smudge = True
                    continue
                return False
            g+=1
        if (is_p2 and has_smudge) or is_p2 == False:
            return True
        return False
    
    def is_smudge(self, line1, line2) -> bool:
        return True if sum(1 for var1, var2 in zip(line1, line2) if var1 != var2) == 1 else False

one = PointOfIncidence('real.txt')
print('Part One:', one.get_sum(False))

two = PointOfIncidence('real.txt')
print('Part Two:', two.get_sum(True))