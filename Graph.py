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

    def bfs(self, s):
        if isinstance(s, int):
            s = self.vertices[s]

        for u in self.vertices:
            u.color = "white"
            u.d = float("inf")
            u.predecessor = None

        s.color = "gray"
        s.d = 0

        queue = []
        queue.append(s)

        while queue:
            u = queue.pop(0)  # FIFO

            for v in u.adj:
                if v.color == "white":

                    v.color = "gray"
                    v.d = u.d + 1
                    v.predecessor = u
                    queue.append(v)

            u.color = "black"

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

    def residual_network(self):
        gf = Graph(len(self.vertices), True, True)

        for u in self.vertices:
            for i, v in enumerate(u.adj):
                if u.weights[i] != u.flows[i]:
                    gf.add_edge(u.nid, v.nid, u.weights[i] - u.flows[i])

                if u.flows[i] > 0:
                    gf.add_edge(v.nid, u.nid, u.flows[i])

        return gf

    def has_path(self, s, v, p):
        if isinstance(s, int):
            s = self.vertices[s]
        if isinstance(v, int):
            v = self.vertices[v]

        if v == s:
            p.append(s)

            return True
        elif v.predecessor == None:
            return False
        else:
            res = self.has_path(s, v.predecessor, p)

            p.append(v)

            return res

    def ford_fulkerson(self, s, t):
        f = 0

        for u in self.vertices:
            for i, v in enumerate(u.adj):
                u.flows.append(0)

        gf = self.residual_network()
        gf.bfs(s)  # bfs for pathfinding
        p = []  # path
        gf.has_path(s, t, p)  # populates path (empty if t unreachable from s)

        while p:
            cf = float("inf")  # residual capacity

            # finds minimum residual capacity in path
            for i, u in enumerate(p):
                for j, v in enumerate(u.adj):
                    if v not in p[:i] and v in p and u.weights[j] < cf:
                        cf = u.weights[j]

            # augments edges in path
            print(f"Augmenting path {[x.nid for x in p]} by {cf}")
            for i, u in enumerate(p):
                for v in u.adj:
                    if v in p and v not in p[:i]:  # second part excludes back edges
                        for j, v_og in enumerate(self.vertices[u.nid].adj):
                            if v.nid == v_og.nid:
                                self.vertices[u.nid].flows[j] += cf

                                break
                        else:  # if (u, v) in path not in G.E
                            for j, u_og in enumerate(self.vertices[v.nid].adj):
                                if u.nid == u_og.nid:  # this is (v, u)
                                    self.vertices[v.nid].flows[j] -= cf

                                    break

            f += cf

            # updates residual network after augmentation
            gf = self.residual_network()
            gf.bfs(s)
            p.clear()
            gf.has_path(s, t, p)

        return f


class Vertex:
    def __init__(self, nid):
        self.nid = nid
        self.adj = []
        self.weights = []  # parallel to adjacency list, capacity in flow problems
        self.flows = []

    def __str__(self):
        return str(self.nid)
