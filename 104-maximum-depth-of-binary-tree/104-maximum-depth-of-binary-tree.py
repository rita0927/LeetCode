# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not root:
#             return 0
        
#         return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
        
 
        
        
        
#         self.depth = 0
#         stack = [(root, 0)]
        
#         while stack:
#             node, localDepth = stack.pop()
            
#             if not node:
#                 self.depth = max(self.depth, localDepth)
#                 continue
            
#             stack.append((node.left, localDepth + 1))
#             stack.append((node.right, localDepth +1))
            
#         return self.depth
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         self.depth = 0
        
#         def dfs(node, localDepth):
#             if not node:
#                 self.depth = max(self.depth, localDepth)
#                 return 
            
#             dfs(node.left, localDepth + 1)
#             dfs(node.right, localDepth + 1)
            
#         dfs(root, 0)
#         return self.depth
    
    
            
            
        
