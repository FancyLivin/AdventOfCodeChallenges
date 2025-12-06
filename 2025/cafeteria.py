from fileReader import readFile

def findFreshIngredients(file: str) -> None:
    data = readFile(file)
    # ingredient range & ingredient id separator index
    separator = data.index("")
    fresh_ranges = mergeRanges(storeRanges(separator, data))
    food_ids = storeIDs(separator, data)

    # Nested loop needed for part one
    # Part two utilizes only initial loop
    current_fresh = 0
    total_fresh = 0
    for interval in fresh_ranges:
        total_fresh += (interval[1] - interval[0] + 1)
        for ingredient in food_ids:
            if interval[0] <= ingredient <= interval[1]:
                current_fresh +=1

    print("Part One:", current_fresh, "Part Two:", total_fresh)

def storeRanges(separator: str, ingredient_data: list) -> list:
    ranges = []
    for x in range(separator):
        low, high = ingredient_data[x].split("-")
        ranges.append([int(low),int(high)])
    return ranges

def storeIDs(separator: str, ingredient_data: list) -> list:
    food_ids = []
    for x in range(separator+1, len(ingredient_data)):
        food_ids.append(int(ingredient_data[x]))
    return food_ids

def mergeRanges(ranges: list) -> list:
    ranges.sort(key=lambda x: x[0]) # sort intervals by starting index
    merged = []
    for interval in ranges:
        if not merged or interval[0] > merged[-1][1]+1:
            merged.append(interval)
        else:
            start = min(merged[-1][0], interval[0])
            end = max(merged[-1][1], interval[1])
            merged[-1] = [start, end]
    return merged

findFreshIngredients("testInputs/cafeteriaOne.txt")
findFreshIngredients("puzzleInputs/cafeteria.txt")