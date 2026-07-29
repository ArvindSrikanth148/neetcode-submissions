class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj=defaultdict(list)
        for u,v, t in flights:
            adj[u].append((v,t))


        best={}
        ans = float("inf")

        def dfs(node, c,stop):
            nonlocal ans
            if stop>k+1:
                return 

            if c>=ans:
                return
            
            if node==dst: 
                ans=min(c,ans)
                return
            
            if (n,stop) in best and  best[(node,stop)]<=c:
                return
            best[(node,stop)]=c

            for nei, t in adj[node]: 
                dfs(nei,c+t,stop+1)

        dfs(src,0,0)
        return -1 if ans == float("inf") else ans
