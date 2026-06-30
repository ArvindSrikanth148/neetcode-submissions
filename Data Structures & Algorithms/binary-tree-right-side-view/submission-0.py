# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q= collections.deque()

        res=[]
        q.append(root)

        while q: 

            l=[]
            for i in range(len(q)):
                node=q.popleft()
                if node: 
                    l.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if l: 
                res.append(l)

        ans=[]
        for i in range(len(res)):
            ans.append(res[i][-1])
        return ans

