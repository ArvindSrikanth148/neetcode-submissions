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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        uf=UnionFind(n)

        for u,v in edges: 
            p=uf.union(u,v)

        return len(set(uf.find(i) for i in range(n)))

        
        


        