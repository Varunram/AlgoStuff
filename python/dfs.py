import sets
# Initizliaze an adjacency list
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


''' Wat 1
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

    return visited

print dfs(graph, 'A')
'''
'''Way 2- Recursice approach
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

print dfs(graph, 'A')
'''
# But this gives only one path traversed from a vertex. Can we get all paths?
'''
Way 3- Getting the paths
def dfs_paths(start, graph, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path+[next]))

print list(dfs_paths('A', graph, 'F'))
'''
'''
Way 4- Using the new yield from syntax in python
def dfs_paths(graph, start, goal, path=None):
    if path is None:
        next = [start]
    if path == goal:
        yield path
    for path in graph[start] - set(path):
        dfs_paths(graph, next, goal, path + [next])
print list(dfs_paths(graph, 'A', 'F'))
'''
