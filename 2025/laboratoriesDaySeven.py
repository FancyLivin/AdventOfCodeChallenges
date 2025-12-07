from fileReader import readFile

def changeEmptyValuesToInt(file: str) -> list[list]:
    diagram = readFile(file)
    for x, line in enumerate(diagram):
        row = list(line)
        for i in range(len(row)):
            row[i] = 0 if row[i] == "." else row[i]
        diagram[x] = row
    return diagram

def printTotalBeamSplits(diagram: list[list]) -> None:
    total_splits = 0
    for x in range(len(diagram)-1):
        for y in range(len(diagram[0])):
            left = right = y
            curr = diagram[x][y]
            if curr == "S":
                diagram[x+1][y] = 1
            if type(curr) == int and curr > 0:
                if diagram[x+1][y] == "^":
                    total_splits +=1
                    left -=1
                    right +=1
                if left == right:
                    diagram[x+1][y] += curr
                else:
                    diagram[x+1][left] += curr
                    diagram[x+1][right] += curr
    print("Part One:", total_splits, "Part Two:", sum(diagram[-1]))