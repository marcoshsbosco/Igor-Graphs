"""
Written for and tested with Python 3.10.4 by Bosco
"""

from Graph import *

# test 1 ------------------------------------------
g = Graph(vertices=9, directed=False, weighted=True)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 5, 4)
g.add_edge(2, 8, 2)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)


print("*-------------------- Graph g --------------------*")
print(g)

g.to_matrix()

print("----- Matrix of g -----")
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

print("\n----- Prim on g -----")
a = g.prim(r=0)

for x in a:
    print(f"{x[1]} - {x[0]} (w={x[0].key})")

print("\n----- Ford-Fulkerson on g -----")
print(f"Maximum flow: {g.ford_fulkerson(0, 8)}")


# test 2 ------------------------------------------
g = Graph(vertices=6, directed=True, weighted=True)
g.add_edge(0, 1, 16)
g.add_edge(0, 2, 13)
g.add_edge(1, 3, 12)
g.add_edge(2, 1, 4)
g.add_edge(2, 4, 14)
g.add_edge(3, 2, 9)
g.add_edge(3, 5, 20)
g.add_edge(4, 3, 7)
g.add_edge(4, 5, 4)

print("\n*-------------------- Graph g --------------------*")
print(g)

g.to_matrix()

print("----- Matrix of g -----")
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

print("\n----- Prim on g -----")
a = g.prim(r=0)

for x in a:
    print(f"{x[1]} - {x[0]} (w={x[0].key})")

print("\n----- Ford-Fulkerson on g -----")
print(f"Maximum flow: {g.ford_fulkerson(0, 5)}")
