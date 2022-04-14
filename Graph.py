class Graph:
    def __init__(self, vertices: int, directed: bool, weighted: bool):
        self.vertices = [Vertex(u) for u in range(vertices)]  # adjacency list
        self.directed = directed
        self.weighted = weighted

    def add_edge(self, u, v, w=None):
        self.vertices[u].adj.append(self.vertices[v])

        if not self.directed:
            self.vertices[v].adj.append(self.vertices[u])

        if self.weighted:
            self.vertices[u].weights.append(w)

            if not self.directed:
                self.vertices[v].weights.append(w)

    def to_matrix(self):
        self.w = [[float("inf") for i in range(len(self.vertices))] for j in range(len(self.vertices))]

        for u in self.vertices:
            if self.weighted:
                self.w[u.nid][u.nid] = 0

            for i, v in enumerate(u.adj):
                if self.weighted:
                    self.w[u.nid][v.nid] = u.weights[i]
                else:
                    self.w[u.nid][v.nid] = 1

    def print_matrix(self):
        for i in self.w:
            s = ""

            for j in i:
                s += f"{j:03} "

            print(s)

    def __str__(self):
        s = ""

        for u in self.vertices:
            s += f"{u}: ["

            for i, v in enumerate(u.adj):
                if not self.weighted:
                    s += f" {v} "
                else:
                    s += f" {v}(w={u.weights[i]}) "

            s += "]\n"

        return s

    def floyd_warshall(self):
        d = self.w.copy()  # shortest-path weights
        p = [[None for i in range(len(self.w))] for j in range(len(self.w))]  # predecessor

        for i in range(len(self.w)):
            for j in range(len(self.w)):
                if i != j and self.w[i][j] < float("inf"):
                    p[i][j] = i

        for k in range(len(self.w)):
            for i in range(len(self.w)):
                for j in range(len(self.w)):
                    if d[i][j] > d[i][k] + d[k][j]:
                        d[i][j] = d[i][k] + d[k][j]
                        p[i][j] = p[k][j]

        return d, p

    def prim(self, r):
        global v_alpha

        if isinstance(r, int):
            r = self.vertices[r]

        for u in self.vertices:
            u.key = float("inf")
            u.predecessor = None

        r.key = 0

        queue = self.vertices.copy()

        while queue:
            u = queue.pop(queue.index(min(queue, key=lambda x:x.key)))

            for i, v in enumerate(u.adj):
                if v in queue and u.weights[i] < v.key:
                    v.predecessor = u
                    v.key = u.weights[i]

        a = []
        for u in self.vertices:
            if u is not r:
                a.append((u, u.predecessor))

        return a


class Vertex:
    def __init__(self, nid):
        self.nid = nid
        self.adj = []
        self.weights = []  # parallel to adjacency list

    def __str__(self):
        return str(self.nid)
