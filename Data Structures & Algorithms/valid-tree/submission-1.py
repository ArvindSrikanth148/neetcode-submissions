class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges)!=n-1:
            return False 
        visited=set()
        q=collections.deque()
        adj=defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in adj[node]:
                dfs(nei)

        dfs(0)
       
        return len(visited)==n
