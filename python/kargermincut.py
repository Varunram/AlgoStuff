from random import choice
from collections import Counter
from copy import deepcopy

def mincut(graph):
	while len(graph) > 2:

		randomVertex = choice(graph.keys())
		graphAtRandomVertex = graph[randomVertex]

		v = graphAtRandomVertex.most_common(1)[0][0]
		graphAtCommonVertex = graph[v]

		del graph[v]

		del graphAtCommonVertex[randomVertex]
		del graphAtRandomVertex[v]

		graphAtRandomVertex.update(graphAtCommonVertex)
		for var in graphAtCommonVertex:
			temp = graph[var]
			temp[randomVertex] += temp[v]
			del temp[v]

	return graph.itervalues().next().most_common(1)[0][1]

def makeadjlist(filename):
    graph={}
    with open(filename) as graphInput:
        for line in graphInput:
            integerArray = [int(x) for x in line.split()]
            graph[integerArray[0]] = Counter(integerArray[1:])

    return graph

graph = makeadjlist('karger.txt')
cuts = [mincut(deepcopy(graph)) for _ in range(100)]
print min(cuts)
