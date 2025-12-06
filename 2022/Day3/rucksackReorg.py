# Conversion of character to int value
# print((ord('a') - 19) % 26 + 1) # Lowercase characters work
# print((ord('Z') + 13) % 52 + 1) # Uppercase characters work

##### PART 1 #####
def rucksackOne():
    file = open("rucksackList.txt", "r")

    prioritySum = 0

    for x in file:
        # Splitting up current rucksack
        compOne = x[:len(x)//2]
        compTwo = x[len(x)//2:]

        # Logic for finding matching unique character in both splits of current rucksack
        for i in compTwo:
            if i in compOne:
                if i.islower():
                    prioritySum += (ord(i) - 19) % 26 + 1
                else:
                    prioritySum += (ord(i) + 13) % 52 + 1
                break

    file.close()
    return prioritySum

##### PART 2 #####
def rucksackTwo():
    file = open("rucksackList.txt", "r")

    prioritySum = 0

    elfOne = ''
    elfTwo = ''
    elfThree = ''

    for count, x in enumerate(file):
        # Assigning elves to correct rucksack lists
        if (count % 3) == 0:
            elfOne = x
        if (count % 3) - 1 == 0:
            elfTwo = x
        if (count % 3) - 2 == 0:
            elfThree = x

            # Logic for finding unique character that matches in all three rucksacks
            for i in elfThree:
                if i in elfOne and i in elfTwo:
                    if i.islower():
                        prioritySum += (ord(i) - 19) % 26 + 1
                    else:
                        prioritySum += (ord(i) + 13) % 52 + 1
                    break  

    file.close()
    return prioritySum

##### PART 1/2 OUTPUT #####
print("Part one answer: " + rucksackOne())
print("Part two answer: " + rucksackTwo())