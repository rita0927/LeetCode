# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = float('-inf')
        
        def findSum(node):
            nonlocal res 
            
            if not node:
                return 0
            
            left = max(findSum(node.left), 0)
            right = max(findSum(node.right), 0)

            res = max(res, left + right + node.val)
            
            return max(left, right) + node.val
        
        findSum(root)
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#         self.res = float("-inf")
#         self.dfs(root)
#         return self.res

#     def dfs(self, node):
#         if not node:
#             return 0

#         left = max(self.dfs(node.left), 0)
#         right = max(self.dfs(node.right), 0)
#         self.res = max(self.res, left + right + node.val)
#         return max(left, right) + node.val