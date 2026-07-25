class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit={}

        def bfs(r,c):
            visited= set()

            q=collections.deque()
            visited.add((r,c))
            visit[(r,c)]=0
            q.append((r,c,0))

            while q: 

                row , col, pos =q.popleft()
                dirs=[[1,0],[0,1],[-1,0],[0,-1]]
                for dr,dc in dirs: 
                    R,C= row+dr,col+dc
                    if R in range(rows) and C in range(cols) and grid[R][C]==1 and (R,C) not in visited:
                        q.append((R,C,pos+1))
                        visited.add((R,C))
                        if (R,C) in visit:
                            visit[(R,C)]=min(visit[(R,C)],pos+1)
                        else: 
                            visit[(R,C)]=pos+1
                        
        maxi=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    bfs(r,c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit: 
                    return -1
        if len(visit.values())==0:
            return 0
        return max(visit.values())

                


