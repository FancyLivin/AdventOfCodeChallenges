##### PART 1 #####
def cleanupOne():
    file = open("campCleanup.txt", "r")

    fullyContained = 0

    for x in file:
        # Creating two elf arrays for future logic
        sections = x.split(",")
        elfOne = sections[0].split("-")
        elfTwo = sections[1].split("-")
        
        # Logic for finding fully overlapping individuals
        if int(elfOne[0]) >= int(elfTwo[0]) and int(elfOne[1]) <= int(elfTwo[1]):
            fullyContained += 1
        elif int(elfTwo[0]) >= int(elfOne[0]) and int(elfTwo[1]) <= int(elfOne[1]):
            fullyContained += 1

    file.close()
    return fullyContained

##### PART 2 #####
def cleanupTwo():
    file = open("campCleanup.txt", "r")

    partiallyContained = 0

    for x in file:
        # Creating two elf arrays for future logic
        sections = x.split(",")
        elfOne = sections[0].split("-")
        elfTwo = sections[1].split("-")

        # Logic for finding partially overlapping individuals
        if int(elfTwo[0]) <= int(elfOne[0]) <= int(elfTwo[1]):
            partiallyContained += 1
        elif int(elfTwo[0]) <= int(elfOne[1]) <= int(elfTwo[1]):
            partiallyContained += 1
        elif int(elfOne[0]) <= int(elfTwo[0]) <= int(elfOne[1]):
            partiallyContained += 1
        elif int(elfOne[0]) <= int(elfTwo[1]) <= int(elfOne[1]):
            partiallyContained += 1

    file.close()
    return partiallyContained

##### PART 1/2 OUTPUT #####
print("Part one answer: " + cleanupOne())
print("Part two answer: " + cleanupTwo())