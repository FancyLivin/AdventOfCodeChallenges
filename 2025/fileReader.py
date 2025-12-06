def readFile(file_name):
    with open(file_name, 'r') as file:
        return file.read().splitlines()