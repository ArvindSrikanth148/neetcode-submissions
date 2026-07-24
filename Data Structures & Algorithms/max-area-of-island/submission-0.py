class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited=set()
        islands= 0 

        def bfs (r,c): 
            q=collections.deque()
            visited.add((r,c))
            q.append((r,c))
            sum=0
            while q: 
                row , col =q.popleft()
                sum=sum+1
                dirs=[[1,0],[0,1],[-1,0],[0,-1]]
                for dr,dc in dirs: 
                    R,C= row+dr,col+dc
                    if R in range(rows) and C in range(cols) and grid[R][C]==1 and (R,C) not in visited:
                        q.append((R,C))
                        visited.add((R,C))
            return sum 
        maxi=0
        for r in range(rows):
            for c in range(cols): 
                if grid[r][c]==1 and (r,c) not in visited: 
                    n=bfs(r,c)
                    maxi=max(n,maxi)
                    islands+=1
        return maxi

        