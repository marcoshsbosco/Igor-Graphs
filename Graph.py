class Graph:
    def __init__(self, vertices: int, directed: bool):
        self.vertices = [Vertex(u) for u in range(vertices)]
        self.directed = directed

    def add_edge(self, u, v):
        self.vertices[u].adj.append(self.vertices[v])

        if not self.directed:
            self.vertices[v].adj.append(self.vertices[u])

    def __str__(self):
        s = ""

        for u in self.vertices:
            s += f"{str(u)}: ["

            for v in u.adj:
                s += f" {str(v)} "

            s += "]\n"

        return s

    def bfs(self, s):
        if isinstance(s, int):
            s = self.vertices[s]

        for u in self.vertices:
            u.color = "white"
            u.d = float("inf")
            u.predecessor = None

        print(f"Visiting source {str(s)}")
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
                    print(f"\nVisiting vertex {str(v)}...")

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

        print(f"Visiting {str(u)} at t={self.time}...")
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
        print(f"Finished {str(u)} at t={self.time}\n")


class Vertex:
    def __init__(self, nid):
        self.nid = nid
        self.adj = []

    def __str__(self):
        return str(self.nid)
