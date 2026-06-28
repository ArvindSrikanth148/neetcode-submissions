# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            leftheight =self.maxheight(root.left)
            rightheight=self.maxheight(root.right)

            b=abs(leftheight-rightheight)<2
            return b and self.isBalanced(root.left) and self.isBalanced(root.right)
        return True
        
    

        
    def maxheight(self,root):

        if not root: 
            return 0

        return 1+ max(self.maxheight(root.left),self.maxheight(root.right))