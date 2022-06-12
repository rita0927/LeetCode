# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, l, r):
            if not node:
                return True
            
            if node.val <= l or node.val >= r:
                return False 
            
            return helper(node.left, l, node.val) and helper(node.right, node.val, r)
        
        
        
        return helper(root, float('-inf'), float('inf'))
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         stack = [(root, float('-inf'), float('inf'))]
        
#         while stack:
#             node, low, high = stack.pop()
            
#             if node.val <= low or node.val >= high:
#                 return False
            
#             if node.left:
#                 stack.append((node.left, low, node.val))
            
#             if node.right:
#                 stack.append((node.right, node.val, high))
                
#         return True 
            
        
       
        
        
        
        
        
#         def dfs(node, low, high):
            
#             if not node:
#                 return True
            
#             if node.val <= low or node.val >= high:
#                 return False
            
#             return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
#         return dfs(root, float('-inf'), float('inf'))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         stack = [(root, float('-inf'), float('inf'))]
        
#         while stack:
#             node, low, high = stack.pop()
            
#             if not node:
#                 continue
            
#             if node.val <= low or node.val >= high:
#                 return False
            
#             stack.append((node.left, low, node.val))
#             stack.append((node.right, node.val, high))
            
#         return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(N), O(N)
        
#         def helper(node, low, high):
#             if not node:
#                 return True
            
#             if node.val <= low or node.val >= high:
#                 return False
            
#             return helper(node.left, low, node.val) and helper(node.right, node.val, high)
            
        
#         return helper(root, float('-inf'), float('inf'))