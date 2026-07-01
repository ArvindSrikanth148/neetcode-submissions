# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def validate(root,val):
            if not root : 
                return 0
            else:
                if root.val>=val:
                    return 1 + validate(root.left,root.val)+validate(root.right,root.val)
                else:
                    return  validate(root.left,val)+ validate(root.right,val)

        return validate(root,root.val)