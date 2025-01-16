"""
Q. Given a weighted, undirected, and connected graph with V vertices and E edges, your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. The graph is represented by an adjacency list, where each element adj[i] is a vector containing vector of integers. Each vector represents an edge, with the first integer denoting the endpoint of the edge and the second integer denoting the weight of the edge.

Input:
3 3
0 1 5
1 2 3
0 2 1

Output: 4
Explanation:

The Spanning Tree resulting in a weight
of 4 is shown above.
Input: 
2 1
0 1 5

Output: 5 

Explanation: Only one Spanning Tree is possible which has a weight of 5.
"""

class DisjointSet:
    """
    1. findParent
        i. recursively go and find parent->parent->parent
        ii. do path compression direct assign ultimate parent to a node
    2. Unioun
        i. find ultimate parent of u and v (Pu, Pv)
        ii. find the size of Pu and Pv
        iii. connect smaller size to larger size always
        iv. add up all in size
    Time Complexity: O(4α) equivalent to O(1)
    Space Complexity: O(4α) equivalent to O(1)

    ** never use both uniounByRank and uniounBySize at once
    """
    def __init__(self, n):
        self.size = [1] * (n+1)
        self.parent = [i for i in range(n+1)]

    def findParent(self, u):
        if u == self.parent[u]:
            return u
        self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]
    
    def uniounBySize(self, u, v):
        Pu = self.findParent(u)
        Pv = self.findParent(v)
        if Pu == Pv: return
        Su = self.size[Pu]
        Sv = self.size[Pv]

        if Su > Sv:
            self.parent[Pv] = Pu
            self.size[Pu] += self.size[Pv]
        else:
            self.parent[Pu] = Pv
            self.size[Pv] += self.size[Pu]


def krushkals(V, adj):
    """
    Krushkal's Algorithm
    1. sort the edges by weight asc
    2. initialize disjoint set
    3. iterate over edges
    4. if u and v not belong to same parent then increase weight
    Time Complexity: O(E) * O(ElogE)
    Space Complexity: O(E)
    """
    new_adj = []
    for i in range(V):
        for edges in adj[i]:
            new_adj.append([i, edges[0], edges[1]])
            
    new_adj = sorted(new_adj, key=lambda x: x[2])
    print(new_adj)

    totalWeight = 0
    ds = DisjointSet(V)

    for edge in new_adj:
        u, v, wt = edge
        Pu = ds.findParent(u)
        Pv = ds.findParent(v)

        if Pu != Pv:
            totalWeight += wt
            ds.uniounBySize(u, v)
    return totalWeight


V = 7
E = 7
ls = [[0, 1, 3], [1, 3, 3], [2, 4, 6], [4, 5, 6], [3, 6, 8], [2, 6, 9], [1, 5, 10]]

adj = [[] for i in range(V)]
for i in range(E):
    u, v, w = ls[i]
    adj[u].append([v, w])
    adj[v].append([u, w])
print(krushkals(V, adj))
