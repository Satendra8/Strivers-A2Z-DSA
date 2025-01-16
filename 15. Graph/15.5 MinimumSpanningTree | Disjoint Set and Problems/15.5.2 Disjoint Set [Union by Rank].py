class DisjointSet:
    """
    1. findParent
        i. recursively go and find parent->parent->parent
        ii. do path compression direct assign ultimate parent to a node
    2. Unioun
        i. find ultimate parent of u and v (Pu, Pv)
        ii. find the rank of Pu and Pv
        iii. connect smaller rank to larger rank always
        iv. if same rank connect any to any and increment rank by 1
    Time Complexity: O(4α) equivalent to O(1)
    Space Complexity: O(4α) equivalent to O(1)

    ** In uniounByRank the rank is distorted after path compression that's why we use uniounBySize
    """
    def __init__(self, n):
        self.rank = [0] * (n+1)
        self.parent = [i for i in range(n+1)]

    def findParent(self, u):
        if u == self.parent[u]:
            return u
        self.parent[u] = self.findParent(self.parent[u])
        return self.parent[u]
    
    def uniounByRank(self, u, v):
        Pu = self.findParent(u)
        Pv = self.findParent(v)
        if Pu == Pv: return
        Ru = self.rank[Pu]
        Rv = self.rank[Pv]

        if Ru > Rv:
            self.parent[Pv] = Pu
        elif Rv > Ru:
            self.parent[Pu] = Pv
        else:
            self.parent[Pv] = Pu
            self.rank[Pu] += 1

ds = DisjointSet(7)
ds.uniounByRank(1, 2)
ds.uniounByRank(2, 3)
ds.uniounByRank(4, 5)
ds.uniounByRank(6, 7)
ds.uniounByRank(5, 6)
if ds.findParent(3) == ds.findParent(7):
    print("Same")
else:
    print("Not Same")
ds.uniounByRank(3, 7)
if ds.findParent(3) == ds.findParent(7):
    print("Same")
else:
    print("Not Same")
