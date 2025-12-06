# Reading/storing input
with open('treeHouses.txt', 'r') as file:
    treeMap = file.readlines()
    treeMap = [line.split() for line in treeMap]

for count, x in enumerate(treeMap):
    treeMap[count] = x[0]

##### PART 1 #####
# Formula to add all edge trees to visible trees
edgeTrees = (len(treeMap) - 1) * 4

# Function to check if non-edge trees are visible
def isVisible(x, y) -> bool:
    northVis = southVis = westVis = eastVis = 0
    tree = treeMap[x][y]

    for axis in range(len(treeMap)):
        nsTree = treeMap[axis][y]
        weTree = treeMap[x][axis]
        
        if nsTree >= tree and axis > x: northVis = 1 
        if nsTree >= tree and axis < x: southVis = 1 
        if weTree >= tree and axis > y: westVis = 1 
        if weTree >= tree and axis < y: eastVis = 1 

    return False if northVis == southVis == eastVis == westVis == 1 else True

def visibleTreesOne():
    totalVisible = edgeTrees

    for x, treeRow in enumerate(treeMap):
        for y, treeCol in enumerate(treeRow):
            # Edge trees already calculated
            if x == 0 or y == 0:
                None
            elif x == len(treeMap) - 1 or y == len(treeMap) - 1:
                None
            # Update total visible trees if true
            else:
                totalVisible += 1 if isVisible(x, y) else 0

    return totalVisible

##### PART 2 #####
# Logic to calculate scenic score in all cardinal directions
def findScore(x, y) -> int:
    nScore = sScore = wScore = eScore = 0
    tree = treeMap[x][y]

    for south in range(x + 1, len(treeMap)):
        sScore+=1
        if treeMap[south][y] >= tree:
            break
    for north in reversed(range(0, x)):
        nScore+=1
        if treeMap[north][y] >= tree:
            break
    for east in range(y + 1, len(treeMap)):
        eScore+=1
        if treeMap[x][east] >= tree:
            break
    for west in reversed(range(0, y)):
        wScore+=1
        if treeMap[x][west] >= tree:
            break

    # Multiply all cardinal direction scenic scores based on initial point
    return nScore * sScore * wScore * eScore

def visibleTreesTwo():
    scenicScore = 0

    for x, treeRow in enumerate(treeMap):
        for y, treeCol in enumerate(treeRow):
            # Update scenic score if higher score obtained
            newScore = findScore(x, y)
            scenicScore = newScore if newScore > scenicScore else scenicScore

    return scenicScore

##### PART 1/2 OUTPUT #####
print("Part 1 output is:", str(visibleTreesOne()))
print("Part 2 output is:", str(visibleTreesTwo()))