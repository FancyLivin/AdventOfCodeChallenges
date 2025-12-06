from fileReader import readFile

def countZeroes(file: str) -> None:
    code = readFile(file)
    lands_on_zero, passes_zero = 0, 0
    dial = 50
    for rotation in code:
        start_pos = dial
        dial = updateDial(dial, rotation) # part one
        passes_zero += passoversInRotation(start_pos, rotation) # part two
        if dial == 0:
            lands_on_zero +=1
    print("Part One:", lands_on_zero, "Part Two:", passes_zero)

def updateDial(dial: int, rotation: str) -> int:
    turn = int(rotation[1:])
    if rotation[0] == "R":
        dial += turn
    else:
        dial -= turn

    while dial > 99 or dial < 0:
        if dial > 99:
            dial -=100
        else:
            dial +=100
    return dial

def passoversInRotation(start: int, rotation: str) -> int:
    turn = int(rotation[1:])
    if rotation[0] == "R": # right logic
        return (turn + start) // 100
    else: # left logic
        if start == 0:
            return turn // 100
        else:
            return 0 if turn < start else (abs(start - turn) // 100) + 1