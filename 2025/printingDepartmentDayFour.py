from fileReader import readFile

def findTotalMovablePaperRoles(file: str) -> None:
    map = readFile(file)
    # adding border to entire map
    paper_matrix = [["."] * (len(map[0]) + 2)]
    for row in map:
        row = list(row)
        row.insert(0, ".")
        row.append(".")
        paper_matrix.append(row)
    paper_matrix.append(["."] * (len(map[0]) + 2))

    movable_rolls = [-1] # allow while loop to begin, -1 is an impossible value
    while movable_rolls[-1] != 0:
        current_movable_rolls = 0
        for m in range(1, len(paper_matrix)-1):
            for n in range(1, len(paper_matrix[0])-1):
                # skip if empty space in matrix
                if paper_matrix[m][n] == ".":
                    continue

                # check surrounding points around current paper roll
                nearby_rolls = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dy == dx == 0:
                            continue
                        nearby_rolls += isRoll(paper_matrix, m + dy, n + dx)

                if nearby_rolls < 4: # movable if nearby rolls is 3 or less
                    paper_matrix[m][n] = "x"
                    current_movable_rolls +=1
        movable_rolls.append(current_movable_rolls)

        # remove all rolls marked with "x"
        for m in range(1, len(paper_matrix)-1):
            for n in range(1, len(paper_matrix[0])-1):
                if paper_matrix[m][n] == "x":
                    paper_matrix[m][n] = "."
    movable_rolls.remove(-1) # remove impossible value from list
    print("Part One:", movable_rolls[0], "Part Two:", sum(movable_rolls))

def isRoll(matrix: list[list[int]], m: int, n: int) -> bool:
    return True if matrix[m][n] in ["@", "x"] else False

findTotalMovablePaperRoles("testInputs/printingDepartmentOne.txt")
findTotalMovablePaperRoles("puzzleInputs/printingDepartment.txt")