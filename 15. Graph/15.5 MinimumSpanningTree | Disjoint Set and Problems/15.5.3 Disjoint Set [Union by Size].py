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
            self.parent[v] = u
            self.size[u] += self.size[v]
        else:
            self.parent[u] = v
            self.size[v] += self.size[u]

ds = DisjointSet(7)
ds.uniounBySize(1, 2)
ds.uniounBySize(2, 3)
ds.uniounBySize(4, 5)
ds.uniounBySize(6, 7)
ds.uniounBySize(5, 6)
if ds.findParent(3) == ds.findParent(7):
    print("Same")
else:
    print("Not Same")
ds.uniounBySize(3, 7)
if ds.findParent(3) == ds.findParent(7):
    print("Same")
else:
    print("Not Same")
