##### PART 1 #####
def maxCaloriesOne():
    file = open("calories.txt", "r")

    maxCal = 0
    currentElfCal = 0

    # Iterating through each group of numbers to find largest sum
    for x in file:
        if x != "\n":
            currentElfCal += int(x)
        else:
            if maxCal < currentElfCal:
                maxCal = currentElfCal
            currentElfCal = 0

    file.close()
    return maxCal

##### PART 2 #####
def maxCaloriesTwo():
    file = open("calories.txt", "r")

    maxCal1 = 0
    maxCal2 = 0
    maxCal3 = 0
    currentElfCal = 0

    # # Iterating through each group of numbers to find the three largest sums
    for x in file:
        if x != "\n":
            currentElfCal += int(x)
        else:
            if maxCal1 < currentElfCal:
                maxCal3 = maxCal2
                maxCal2 = maxCal1
                maxCal1 = currentElfCal
            elif maxCal2 < currentElfCal:
                maxCal3 = maxCal2
                maxCal2 = currentElfCal
            elif maxCal3 < currentElfCal:
                maxCal3 = currentElfCal
            currentElfCal = 0

    file.close()
    return maxCal1 + maxCal2 + maxCal3

##### PART 1/2 OUTPUT #####
print("Part one answer: " + maxCaloriesOne())
print("Part two answer: " + maxCaloriesTwo())