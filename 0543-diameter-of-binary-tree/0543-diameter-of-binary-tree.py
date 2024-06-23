# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxm = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:    
        self.maxm = 0
        self.findLongestPath(root)
        return self.maxm
        
        
 
        
    def findLongestPath(self, root: Optional[TreeNode]):
        countleft = 0
        countright = 0
        
        if not (root):
            return 0
        
        if root.left:
            countleft = self.findLongestPath(root.left) + 1
        
        if root.right:
            countright = self.findLongestPath(root.right) + 1
        
        new = countleft+countright
        
        if (new > self.maxm):
            self.maxm = new
            
        
        return max(countleft, countright)
            
        
            
        
        
        
        
        
        
        