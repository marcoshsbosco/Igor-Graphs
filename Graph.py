class Graph:
    def __init__(self, vertices: int, directed: bool):
        self.vertices = [Vertex(u) for u in range(vertices)]
        self.directed = directed

    def add_edge(self, u, v):
        if self.directed:
            self.vertices[u].adj.append(self.vertices[v])
        else:
            self.vertices[u].adj.append(self.vertices[v])
            self.vertices[v].adj.append(self.vertices[u])

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
