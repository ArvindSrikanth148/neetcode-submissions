class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: 
            return 0
        
        rows, cols = len(heights), len(heights[0])
        def bfs(starts):
            visited= set(starts)

            q=collections.deque(starts)
            
        

            while q: 

                row , col=q.popleft()
            
                dirs=[[1,0],[0,1],[-1,0],[0,-1]]
                for dr,dc in dirs: 
                    R,C= row+dr,col+dc
                    
                    if R in range(rows) and C in range(cols) and heights[row][col]<=heights[R][C] and (R,C) not in visited:
                        q.append((R,C))
                        visited.add((R,C))
                        
            return visited
        pacific_starts = []
        atlantic_starts = []

        for c in range(cols):
            pacific_starts.append((0, c))
            atlantic_starts.append((rows - 1, c))

        for r in range(rows):
            pacific_starts.append((r, 0))
            atlantic_starts.append((r, cols - 1))

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res

        
       

                    

