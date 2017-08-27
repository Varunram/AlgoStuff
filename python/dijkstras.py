def dijkstra(graph, src, dest, visited =[], distances ={}, predecessors ={}):
    if src not in graph:
        print "Vertex not in graph. Exiting"
        raise TypeError("Exit!")
    if dest not in graph:
        print "Destination is Jurassic World"
        raise TypeError("Exit!")

    if src == dest:
        # build the path to be returned
        path =[]
        pred = dest
        while pred is not None:
            path.append(pred)
            pred = predecessors.get(pred, None)

        print "Shortest path is: " + str(path) + " with a cost of: " + str(distances[dest])

    else:
        if not visited:
            distances[src] = 0
        # do magic
        for neighbor in graph[src]:
            if neighbor not in visited:
                new_dist = distances[src] + graph[src][neighbor]
                if new_dist < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_dist
                    predecessors[neighbor] = src

        visited.append(src)

        unvisited ={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))

        x = min(unvisited, key = unvisited.get)
        dijkstra(graph, x, dest, visited, distances, predecessors)

if __name__ == "__main__":
   graph = {'s': {'a': 2, 'b': 1},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}}
   dijkstra(graph, 's', 't')
