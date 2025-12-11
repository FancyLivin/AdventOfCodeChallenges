from fileReader import readFile

def parseData(file: str) -> list[list[int]]:
    data = readFile(file)
    for i, line in enumerate(data):
        data[i] = list((int(x) for x in line.split(",")))
    return data

def printRectangleAreas(coords: list[list[int]]) -> None:
    edges = createEdges(coords)

    red_tile_max_area = 0
    green_red_tile_max_area = 0

    for i, (x1,y1) in enumerate(coords):
        for j, (x2,y2) in enumerate(coords):
            a = (abs(x1-x2) + 1) * (abs(y1-y2) + 1)
            if i < j:
                min_x, max_x = min(x1,x2), max(x1,x2)
                min_y, max_y = min(y1,y2), max(y1, y2)
                if not isIntersecting(min_x, max_x, min_y, max_y, edges):
                    green_red_tile_max_area = max(green_red_tile_max_area, a)
                red_tile_max_area = max(red_tile_max_area, a)
    print("Part One:", red_tile_max_area, "Part Two:", green_red_tile_max_area)

def createEdges(coords: list[list[int]]) -> list[list[int]]:
    edges = []
    for i in range(-1, len(coords)-1):
        from_point = coords[i]
        to_point = coords[i+1]
        # append from_x, from_y, to_x, to_y respectively
        edges.append([from_point[0], from_point[1], to_point[0], to_point[1]])
    return edges

def isIntersecting(left, right, top, bottom, edges) -> bool:
    for e in edges:
        e_left, e_right = min(e[0], e[2]), max(e[0], e[2])
        e_top, e_bottom = min(e[1], e[3]), max(e[1], e[3])
        if left < e_right and right > e_left and top < e_bottom and bottom > e_top:
            return True
    return False

printRectangleAreas(parseData("testInputs/movieTheaterOne.txt"))
printRectangleAreas(parseData("puzzleInputs/movieTheater.txt"))