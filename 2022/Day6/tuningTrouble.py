##### PART 1/2 #####
def tuningMessage(messageLength):
    file = open("tuningTrouble.txt", "r")

    for x in file:
        packetList = []

        for character in range(len(x)):
            # Edge case for removing the same character near beginning of pattern
            if len(packetList) > len(set(packetList)):
                packetList.pop(0)

            # Logic for finding unique sequential pattern
            if x[character] not in packetList and len(packetList) < messageLength:
                packetList.append(x[character])
            elif x[character] in packetList:
                packetList.pop(0)
                packetList.append(x[character])
            
            # Returns character after found pattern
            if len(packetList) == messageLength:
                file.close()
                return character + 1
        
        # If no pattern is found return -1
        file.close()
        return -1

##### PART 1/2 OUTPUT #####
print("Part one output is: " + str(tuningMessage(4)))
print("Part two output is: " + str(tuningMessage(14)))