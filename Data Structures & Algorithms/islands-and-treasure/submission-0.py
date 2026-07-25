class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        if not grid: 
            return 0
        
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            visited= set()

            q=collections.deque()
            visited.add((r,c))
            q.append((r,c,0))

            while q: 

                row , col, pos =q.popleft()
                dirs=[[1,0],[0,1],[-1,0],[0,-1]]
                for dr,dc in dirs: 
                    R,C= row+dr,col+dc
                    if R in range(rows) and C in range(cols) and grid[R][C]>0 and (R,C) not in visited:
                        grid[R][C]=min(pos+1,grid[R][C])
                        q.append((R,C,pos+1))
                        visited.add((R,C))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    bfs(r,c)
        
                


        