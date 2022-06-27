# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return None
        
        
        res = []
        
        def backtrack(node, path, s):
            path.append(node.val)
            s += node.val
            
            if not node.left and not node.right and s == targetSum:
                res.append(path.copy())
            
            if node.left:
                backtrack(node.left, path, s)
            if node.right:
                backtrack(node.right, path, s)
            path.pop()
            s -= node.val
            
        backtrack(root, [], 0)
        
        return res 

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     # O(N**2) for iterating and copying the nodes
#     # O(N) to keep track of path 
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
#         if not root:
#             return []
        
#         res = []
        
#         def dfs(node, path, s):
#             # if not node:
#             #     return 
#             path.append(node.val)
#             s += node.val
            
#             if not node.left and not node.right and s == targetSum:
#                 res.append(path.copy())
                
#             if node.left:
#                 dfs(node.left, path, s)
#             if node.right:
#                 dfs(node.right, path, s)
            
#             path.pop()
#             s -= node.val

        
#         dfs(root, [], 0)
#         return res 
                
                
            
        