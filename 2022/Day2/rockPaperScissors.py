##### PART 1 #####
# MOVES (X, Y, Z is player)
# MOVES (A, B, C is elf/opponent)
# A = X = Rock
# B = Y = Paper
# C = Z = Scissors

# POINTS
# Rock(1), Paper(2), Scissors(3)
# Win (6), Draw (3), Lose(0)

def rpsSumOne():
    rpsList = open("rpsPuzzleInput.txt", "r")

    totalScore = 0
    # Stores all game moves as integer values
    convertMove = {
        "X": 1, "A": 0,
        "Y": 2, "B": 1,
        "Z": 3, "C": 2
    }

    # Iterates through every match found in .txt file
    for x in rpsList:
        # Grab string value for player/elf moves
        pMove = x[2]
        eMove = x[0]

        # Grab integer value of player/elf moves based on dictionary
        pScore = convertMove.get(pMove)
        eScore = convertMove.get(eMove)

        # Calculates game outcome and uses that to add to score sum
        gameWinner = (pScore - eScore) % 3
        totalScore += pScore + (3 * gameWinner)
    return totalScore

##### PART 2 #####
# GAME OUTCOME
# X = LOSE(0), Y = DRAW(3), Z = WIN(6)
# A, B, C REMAINS UNCHANGED

def rpsSumTwo():
    rpsList = open("rpsPuzzleInput.txt", "r")

    totalScore = 0
    # Stores all game moves and additional information as integer values
    convertMove = {
        "X": {"output": 0, "addOn": 1}, "A": 1,
        "Y": {"output": 3, "addOn": 2}, "B": 2,
        "Z": {"output": 6, "addOn": 0}, "C": 3
    }

    # Iterates through every match found in .txt file
    for x in rpsList:
        # Grab string value for elf move and game outcome
        gameOutcome = x[2]
        eMove = x[0]

        # Used to calculate player score based on elf move
        outcome = convertMove.get(gameOutcome).get("output")
        addOnValue = convertMove.get(gameOutcome).get("addOn") # Necessary for score calculation based on game outcome
        # Integer value of elf's move
        eScore = convertMove.get(eMove)

        # Adds previous three values to score sum based on match outcome
        totalScore += ((eScore + addOnValue) % 3 + 1) + outcome
    return totalScore

##### PART 1/2 OUTPUT #####
print("Part One total is " + str(rpsSumOne()))
print("Part Two total is " + str(rpsSumTwo()))
