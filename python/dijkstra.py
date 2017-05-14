nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
dists = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}

unvisited = {node: float('inf') for node in nodes}
visited = {}
given = 'A'

prevdistance =0
unvisited[given] = prevdistance
visited ={}

while True:
    for neighbor, distance in dists[given].items():
        if neighbor not in unvisited: continue
        newdistance = prevdistance + distance
        if unvisited[neighbor] is float('inf') or unvisited[neighbor] > newdistance:
            unvisited[neighbor] = newdistance

    visited[given] = prevdistance
    del unvisited[given]
    if not unvisited: break
    given, prevdistance = sorted(unvisited.items(), key =lambda x: x[1])[0]

print(visited)
