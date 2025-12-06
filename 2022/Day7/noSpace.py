from nonBinaryTree import Node, NonBinaryTree

def readFile():
    with open("noSpace.txt", "r") as file:
        lines = file.readlines()
        lines = [single_line.strip() for single_line in lines]
    return lines

def dirUp(directory):
    None

def dirDown(directory):
    None

def dirRoot():
    return '/', None

def changeDir(directory, current, parent, child):
    None

def arrangeFileSys():
    commandLines = readFile()
    fileSys = {'/': {}}
    currentDir = '/'
    parentDir = None

    while len(commandLines) > 0:
        command = commandLines.pop(0)
        if command[:4] == '$ cd':
            if command[4:] == ' /':
                currentDir, parentDir = dirRoot()
            elif command[4:] == ' ..':
                None
            else:
                _, _, dirName = command.split()

        elif command == '$ ls':
            while len(commandLines) > 0 and commandLines[0][0] != '$':
                command = commandLines.pop(0)
                size, name = command.split()
                if size == 'dir':
                    fileSys[currentDir][name] = {}
                    None
                else:
                    fileSys[currentDir][name] = size
                    None
                
            # break
    return fileSys

print(arrangeFileSys())

##### PART 1 #####
def noSpaceOne():
    dirSizeSum = 0
    
    return dirSizeSum

##### PART 2 #####
def noSpaceTwo():
    return None

##### PART 1/2 OUTPUT ######
# print("Output for Part 1:",str(noSpaceOne()))
# print("Output for Part 2:",str(noSpaceTwo()))