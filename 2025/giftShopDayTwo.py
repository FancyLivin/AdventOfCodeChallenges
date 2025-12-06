from fileReader import readFile

def sumAllInvalidIDs(file: str) -> None:
    ranges = readFile(file)[0].split(",")
    part_one_sum, part_two_sum = 0, 0
    for r in ranges:
        # skipping past newline at end of file if present
        if r == "":
            continue
        start, end = r.split("-")
        part_one_sum += checkRangeForSplitSequenceInvalidIDs(int(start), int(end))
        part_two_sum += checkRangeForAllInvalidIDs(int(start), int(end))
    print("Part One:", part_one_sum, "Part Two:", part_two_sum)

def checkRangeForSplitSequenceInvalidIDs(start: int, end: int) -> int:
    rangeSum = 0
    for x in range(start, end + 1):
        isInvalid = True
        x = str(x)
        if len(x) % 2 == 1:
            continue
        r = len(x) - 1
        for l in range(len(x) // 2 - 1, -1, -1):
            if x[l] != x[r]:
                isInvalid = False
            r -=1
        if isInvalid:
            rangeSum += int(x)
    return rangeSum

def checkRangeForAllInvalidIDs(start: int, end: int) -> int:
    rangeSum = 0
    for num in range(start, end + 1):
        num = str(num)
        for i in range(1, len(num) // 2 + 1):
            if len(num) % i != 0:
                continue
            split_num = []
            for x in range(0, len(num), i):
                split_num.append(num[x:x+i])
            if len(set(split_num)) == 1:
                rangeSum += int(num)
                break
    return rangeSum

sumAllInvalidIDs("testInputs/giftShopTwo.txt")
sumAllInvalidIDs("testInputs/giftShopOne.txt")
sumAllInvalidIDs("puzzleInputs/giftShop.txt")