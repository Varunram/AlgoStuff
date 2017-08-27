from sys import maxint


class BellmanFord(object):
    def __init__(self):
        print "Ready to go"

    def shortestPath(self, weight, source):

        size = len(weight)
        eve = -1
        infinity = maxint

        pred = [eve] * size
        mindist = [infinity] * size

        mindist[source] =0

        for i in range(1, size - 1):
            for v in range(size):
                for x in self.adjacency(weight, v):
                    if mindist[x] > mindist[v] + weight[v][x]:
                        mindist[x] = mindist[v] + weight[v][x]
                        pred[x] = v

        for v in range(size):
            for x in self.adjacency(weight, v):
                if mindist[x] > mindist[v] + weight[v][x]:
                    raise Excpetion("Negative cycle found")

        return [pred, mindist]

    def adjacency(self, g, v):
        result = []
        for x in range(len(g)):
            if g[v][x] is not None:
                result.append(x)

        return result


weight = [
    [None, -1, 4, None, None],
    [None, None, 3, 2, 2],
    [None, None, None, None, None],
    [None, 1, 5, None, None],
    [None, None, None, -3, None]
]
source = 0
rnd = BellmanFord()
result = rnd.shortestPath(weight, source)
print result
