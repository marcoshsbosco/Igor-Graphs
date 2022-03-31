from Graph import *

g = Graph(vertices=7, directed=True)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

print("----- Graph g -----")
print(g)

print("----- BFS on g -----")
g.bfs(s=0)

print("\n----- DFS on g -----")
g.dfs()
