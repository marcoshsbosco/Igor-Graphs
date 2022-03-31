class Graph:
    def __init__(self, vertices):
        self.vertices = [Vertex(u) for u in range(vertices)]

    def add_edge(self, u, v):
        self.vertices[u].adj.append(self.vertices[v])

    def __str__(self):
        s = ""

        for u in self.vertices:
            s += f"{str(u)}: ["

            for v in u.adj:
                s += f" {str(v)} "

            s += "]\n"

        return s

class Vertex:
    def __init__(self, nid):
        self.nid = nid
        self.adj = []

    def __str__(self):
        return str(self.nid)
