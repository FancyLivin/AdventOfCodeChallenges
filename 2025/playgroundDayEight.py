from fileReader import readFile
from math import prod

# output utlized in displayCircuits function
def parseCoords(file: str) -> list[tuple[int]]:
    coords = readFile(file)
    for i, line in enumerate(coords):
        coords[i] = tuple(int(x) for x in line.split(","))
    return coords

def displayCircuits(coords: list[tuple[int]], shortest_connections: int) -> None:
    # get all unique connections
    unique_connections = {}
    for i, (x1,y1,z1) in enumerate(coords):
        for j, (x2,y2,z2) in enumerate(coords):
            distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2))
            if i < j:
                unique_connections[i,j] = distance

    # sort all connections in ascending order by distance
    smallest_distances = []
    for point, distance in unique_connections.items():
        smallest_distances.append([distance, point[0], point[1]])
    smallest_distances.sort(key=lambda x: x[0])

    circuits = partOne(smallest_distances[:shortest_connections])
    last_two_junctions_prod = partTwo(smallest_distances, coords)
    print("Part One:", prod([len(x) for x in circuits[:3]]), "Part Two:", last_two_junctions_prod)

def partOne(distances: list) -> list[set[int]]:
    # populate circuits with smallest connections
    circuits = []
    for _, p1, p2 in distances:
        circuits.append(set([p1, p2]))

    # union non-disjoint sets
    changed = True
    while changed:
        changed = False
        for i in range(len(circuits)):
            for j in range(i+1, len(circuits)):
                if not circuits[i].isdisjoint(circuits[j]):
                    circuits[i] |= circuits[j] # updates set x with set y
                    circuits[j].clear()
                    changed = True

    # sort circuits by largest length and removed empty sets
    circuits.sort(key=lambda x: len(x), reverse=True)
    while circuits[-1] == set():
        circuits.pop()
    return circuits

def partTwo(distances: list, coords: list[tuple[int]]) -> int:
    seen = set()
    for _, p1, p2 in distances:
        seen.update([p1, p2])
        if len(seen) == len(coords):
            return (coords[p1][0] * coords[p2][0])