class UnionFind: 
    def __init__(self, n): 
        self.parent =[i for i in range(n)]

    def find(self,x): 

        while x!=self.parent[x]: 
            x=self.parent[x]
        return x
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False      

        self.parent[rootY] = rootX
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        
        uf=UnionFind(len(edges))

        for u,v in edges: 
            p=uf.union(u-1,v-1)
            if not p:
                return [u,v]













        