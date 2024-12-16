"""
Theory :

How to Store Graph
1. Matrix
2. List

1. Matrix Method
n = 5, m = 6

Edges: 
1 2
1 3
2 4
3 4
3 5
4 5

Space Complexity: N*N (costly)

[
    0  1  2  3  4  5
0  [0, 0, 0, 0, 0, 0],
1  [0, 0, 1, 1, 0, 0],
2  [0, 1, 0, 0, 1, 0],
3  [0, 1, 0, 0, 1, 1],
4  [0, 0, 1, 1, 0, 1],
5  [0, 0, 0, 1, 1, 0]

]
"""
n = int(input("Number of vertices"))
m = int(input("Number of edges"))

adj = [[0] * (n+1) for _ in range(n+1)]
print(adj)

for i in range(m):
    u, v = map(int, input("Enter Edges").split())
    adj[u][v] = 1
    adj[v][u] = 1

print(adj)


"""
1. List Method
n = 5, m = 6

Edges: 
1 2
1 3
2 4
3 4
3 5
4 5

Space Complexity: O(2E) # every edge has 2 nodes

0 --> {}
1 --> {2,3}
2 --> {1,4}
3 --> {1,4,5}
4 --> {2,3,5}
5 --> {3,4}

"""

n = int(input("Number of vertices"))
m = int(input("Number of edges"))

l = {i: set() for i in range(n+1)}

for i in range(m):
    u,v = map(int, input("Enter Edges").split())
    l[u].add(v)
    l[v].add(u)
print(l)


"""
Q. Given an integer n representing number of vertices. Find out how many undirected graphs (not necessarily connected) can be constructed out of a given n number of vertices.

Example 1:

Input: 2
Output: 2

Example 2:

Input: 5
Output: 1024
"""

def count(n):
    """
    In a graph G with n vertices, maixmum number of edges possible = n(n-1)/2
    There are two ways for a edge, (the edge may appear in graph or may absent in graph).
    So there are two options for each edge.

    Total number of graphs with n vertices = 2 ** n(n-1)/2
    """
    return 2 ** int((n*(n-1))/2)


n = 5
print(count(n))


