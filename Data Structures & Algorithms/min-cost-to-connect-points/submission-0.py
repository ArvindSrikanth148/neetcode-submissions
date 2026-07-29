class UnionFind: 
    def __init__(self, n): 
        self.parent =[i for i in range(n+1)]
        self.Size=[1]*((n+1))


    def find(self,x): 

        while x!=self.parent[x]: 
            x=self.parent[x]
        return x
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False 
        if self.Size[rootX]<self.Size[rootY]:
            rootX,rootY=rootY,rootX

        self.Size[rootY]+=self.Size[rootX]
        self.parent[rootY]=rootX     
        return True
 



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n=len(points)
        uf=UnionFind(n)
        edges=[]
        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))

        edges.sort()
        res=0

        for dist, u,v in edges: 
            if uf.union(u,v):
                res=res+dist
        return res




        












        
        