from Graph import *

# test 1 ------------------------------------------
g = Graph(vertices=5, directed=True, weighted=True)
g.add_edge(0, 1, 3)
g.add_edge(0, 2, 8)
g.add_edge(0, 4, -4)
g.add_edge(1, 3, 1)
g.add_edge(1, 4, 7)
g.add_edge(2, 1, 4)
g.add_edge(3, 0, 2)
g.add_edge(3, 2, -5)
g.add_edge(4, 3, 6)

print("*-------------------- Graph g1 --------------------*")
print(g)

print("----- BFS on g -----")
g.bfs(s=0)

print("\n----- DFS on g -----")
g.dfs()

g.to_matrix()

print("\n----- Matrix of g -----")
g.print_matrix()

print("\n----- Floyd-Warshall on g -----")
d, p = g.floyd_warshall()

print("----- d -----")
for i in d:
    s = ""

    for j in i:
        s += f"{j:03} "

    print(s)

print("\n----- p -----")
for i in p:
    s = ""

    for j in i:
        try:
            s += f"{j:03} "
        except TypeError:
            s += "NIL "

    print(s)


# test 2 ------------------------------------------
g = Graph(vertices=6, directed=True, weighted=True)
g.add_edge(0, 4, -1)
g.add_edge(1, 0, 1)
g.add_edge(1, 3, 2)
g.add_edge(2, 1, 2)
g.add_edge(2, 5, -8)
g.add_edge(3, 0, -4)
g.add_edge(3, 4, 3)
g.add_edge(4, 1, 7)
g.add_edge(5, 1, 5)
g.add_edge(5, 2, 10)

print("\n\n*-------------------- Graph g2 --------------------*")
print(g)

print("----- BFS on g -----")
g.bfs(s=0)

print("\n----- DFS on g -----")
g.dfs()

g.to_matrix()

print("\n----- Matrix of g -----")
g.print_matrix()

print("\n----- Floyd-Warshall on g -----")
d, p = g.floyd_warshall()

print("----- d -----")
for i in d:
    s = ""

    for j in i:
        s += f"{j:03} "

    print(s)

print("\n----- p -----")
for i in p:
    s = ""

    for j in i:
        try:
            s += f"{j:03} "
        except TypeError:
            s += "NIL "

    print(s)
