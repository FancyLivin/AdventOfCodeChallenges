from fileReader import readFile

def sumMathProblems(file: str) -> None:
    human_parser = horizontalInputParser(file)
    cephalopod_parser = verticalInputParser(file)

    human_sum = getFullSum(human_parser)
    cephalopod_sum = getFullSum(cephalopod_parser)
    
    print("Part One:", human_sum, "Part Two:", cephalopod_sum)

def horizontalInputParser(file: str) -> list:
    problems = readFile(file)
    for x, line in enumerate(problems):
        problems[x] = line.split()

    human = []
    for y in range(len(problems[0])):
        single_prob = []
        for x in range(len(problems)-1, -1, -1):
            single_prob.append(problems[x][y])
        human.append(single_prob)
    return human

def verticalInputParser(file: str) -> list:
    problems = readFile(file)
    ceph = []
    single_prob = []
    for y in range(len(problems[0])):
        num = ""
        for x in range(len(problems)-1):
            num += problems[x][y]

        operand = problems[-1][y]
        if operand != " ":
            single_prob.append(operand)

        if num.strip() == "":
            ceph.append(single_prob)
            single_prob = []
        else:
            single_prob.append(num)
    ceph.append(single_prob) # skips last append before leaving loop
    return ceph

def getFullSum(parser: list) -> int:
    sum = 0
    for problem in parser:
        operation = problem[0]
        add, mult = 0, 1
        for x in range(1, len(problem)):
            if operation == "*":
                mult *= int(problem[x])
            else:
                mult = 0
                add += int(problem[x])
        sum += (add + mult)
    return sum