"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        first = Node(node.val)
        q = collections.deque([node])
        visited = {node: first}

        while q:
            cur = q.popleft()

            for nei in cur.neighbors:

                if nei not in visited:
                    new = Node(nei.val)
                    visited[nei] = new
                    q.append(nei)

            
                visited[cur].neighbors.append(visited[nei])

        return first