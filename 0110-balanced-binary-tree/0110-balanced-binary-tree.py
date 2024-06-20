# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.preorder(root)[0]
        
    
    
    def preorder(self, root: Optional[TreeNode]) -> int:
        if (root):
            left, right = self.preorder(root.left), self.preorder(root.right)
            
            if ((left[0] and right[0]) == False):
                return [False, None]
            
            return [abs(left[1]-right[1]) <= 1, 1 + max(left[1], right[1])]
        else:    
            return [True, 0]
            
            