from Graph import *

g = Graph(vertices=7, directed=True, weighted=True)
g.add_edge(0, 1, 1)
g.add_edge(0, 2, 2)
g.add_edge(1, 3, 4)
g.add_edge(1, 4, 6)
g.add_edge(2, 5, 8)
g.add_edge(2, 6, 10)

print("----- Graph g -----")
print(g)

print("----- BFS on g -----")
g.bfs(s=0)

print("\n----- DFS on g -----")
g.dfs()

g.to_matrix()

print("\n----- Matrix of g -----")
g.print_matrix()
