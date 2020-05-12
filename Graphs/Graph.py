from Queues import MyQueue

class Vertex:

    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.distance = 0
        self.color = 'white'
        self.pred = None

    def add_neighbour(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_distance(self, distance):
        self.distance = distance

    def get_distance(self):
        return self.distance

    def set_pred(self, vertex):
        self.pred = vertex

    def get_pred(self):
        return self.pred

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

class Graph:

    def __init__(self):
        self.vertex_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        self.num_vertices += 1
        new_vertex = Vertex(key)
        self.vertex_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vertex_list:
            return self.vertex_list[n]
        else:
            return None

    def __contains__(self, item):
        return item in self.vertex_list

    def add_edge(self, f, t, weight=0):
        if f not in self.vertex_list:
            new_vertex = self.add_vertex(f)
        if t not in self.vertex_list:
            new_vertex = self.add_vertex(t)
        self.vertex_list[f].add_neighbour(self.vertex_list[t], weight)
        # if graph is non-directed
        self.vertex_list[t].add_neighbour(self.vertex_list[f], weight)

    def get_vertices(self):
        return self.vertex_list.keys()

    def __iter__(self):
        return iter(self.vertex_list.values())


def bfs(graph, start):
    start.set_distance(0)
    start.set_pred(None)
    vertex_queue = MyQueue.MyQueue()
    vertex_queue.enqueue(start)

    while(vertex_queue.size() > 0):
        current_vertex = vertex_queue.dequeue()
        print("Visiting {}".format(current_vertex))

        for nbr in current_vertex.get_connections():
            print("Neighbour = {}".format(nbr))
            if nbr.get_color() == 'white':
                nbr.set_color('gray')
                nbr.set_distance(current_vertex.get_distance() + 1)
                nbr.set_pred(current_vertex)
                vertex_queue.enqueue(nbr)
                print("size = {}".format(vertex_queue.size()))

        current_vertex.set_color('black')
        print(vertex_queue.size())

def bfs_search(graph, start, target):
    start.set_distance(0)
    start.set_pred(None)
    vertex_queue = MyQueue.MyQueue()
    vertex_queue.enqueue(start)

    while(vertex_queue.size() > 0):
        current_vertex = vertex_queue.dequeue()
        print("Current vertex = {}".format(current_vertex))
        print("Target = {}".format(target))
        print("Eq? {}".format(current_vertex == target))
        if current_vertex == target:
            return "Target found, distance = {}".format(current_vertex.get_distance())

        else:
            for nbr in current_vertex.get_connections():
                if nbr.get_color() == 'white':
                    nbr.set_color('gray')
                    nbr.set_distance(current_vertex.get_distance() + 1)
                    nbr.set_pred(current_vertex)
                    vertex_queue.enqueue(nbr)

            current_vertex.set_color('black')

def dfs(graph, start):
    start.set_distance(0)
    start.set_pred(None)

    start.set_color('black')
    print(start)

    for nbr in start.get_connections():
        if nbr.get_color() != 'black':
            dfs(graph, nbr)

def dfs_search(graph, start, target):
    start.set_distance(0)
    start.set_color('black')


    if start == target:
        return True

    else:
        for nbr in start.get_connections():
            if nbr.get_color() != 'black':
                ans = dfs_search(graph, nbr, target)
                if ans:
                    return True

    return False

if __name__ == '__main__':
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('A', 'D')
    graph.add_edge('D', 'E')

    # for vert in graph:
    #     print(vert)

    v = graph.get_vertex('A')
    target = graph.get_vertex('E')

    # bfs(graph, v)

    # print(bfs_search(graph, v, target))

    # dfs(graph, v)
    print(dfs_search(graph, v, target))