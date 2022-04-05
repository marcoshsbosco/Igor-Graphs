class Graph:
    def __init__(self, vertices: int, directed: bool, weighted: bool):
        self.vertices = [Vertex(u) for u in range(vertices)]
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

    def bfs(self, s):
        if isinstance(s, int):
            s = self.vertices[s]

        for u in self.vertices:
            u.color = "white"
            u.d = float("inf")
            u.predecessor = None

        print(f"Visiting source {s}")
        s.color = "gray"
        s.d = 0
        print(f"d: {s.d}")
        print(f"predecessor: {s.predecessor}")

        queue = []
        queue.append(s)

        while queue:
            u = queue.pop(0)

            for v in u.adj:
                if v.color == "white":
                    print(f"\nVisiting vertex {v}...")

                    v.color = "gray"
                    v.d = u.d + 1
                    v.predecessor = u
                    queue.append(v)

                    print(f"d: {v.d}")
                    print(f"predecessor: {v.predecessor}")

            u.color = "black"

    def dfs(self):
        for u in self.vertices:
            u.color = "white"
            u.predecessor = None

        self.time = 0

        for u in self.vertices:
            if u.color == "white":
                self.dfs_visit(u)

    def dfs_visit(self, u):
        self.time += 1

        print(f"Visiting {u} at t={self.time}...")
        print(f"predecessor: {u.predecessor}\n")

        u.d = self.time
        u.color = "gray"

        for v in u.adj:
            if v.color == "white":
                v.predecessor = u
                self.dfs_visit(v)

        u.color = "black"
        self.time += 1
        u.f = self.time
        print(f"Finished {u} at t={self.time}\n")

    def floyd_warshall(self):
        d = self.w.copy()
        p = [[None for i in range(len(self.w))] for j in range(len(self.w))]

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


class Vertex:
    def __init__(self, nid):
        self.nid = nid
        self.adj = []
        self.weights = []

    def __str__(self):
        return str(self.nid)
