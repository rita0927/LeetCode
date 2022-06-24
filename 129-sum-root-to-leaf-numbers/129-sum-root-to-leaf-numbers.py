# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        
        def dfs(node, cur):
            nonlocal total 
            if not node:
                return
            cur = cur * 10 + node.val
            
            if not node.left and not node.right:
                total += cur
                return 
            
            dfs(node.left, cur)
            dfs(node.right, cur)
        
        dfs(root, 0)
        return total 
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = 0
#         stack = [(root, 0)]
        
#         while stack:
#             node, cur = stack.pop()
                
#             cur = cur * 10 + node.val

#             if not node.left and not node.right:
#                 res += cur
#             if node.left:
#                 stack.append((node.left, cur))
#             if node.right:
#                 stack.append((node.right, cur))
#         return res 
                
                
                
        

            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(n), O(h)
        
#         total = 0
#         def dfs(node, cur):
#             nonlocal total 
#             if not node:
#                 return
            
#             cur = cur * 10 + node.val
            
#             if not node.left and not node.right:
#                 total += cur
#                 return
            
#             dfs(node.left, cur)
#             dfs(node.right, cur)
            
#         dfs(root, 0)
#         return total 
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def helper(root, sum):
#             if not root:
#                 return 0
#             sum = sum * 10 + root.val
#             if not root.left and not root.right:
#                 return sum
#             return helper(root.left, sum) + helper(root.right, sum)

#         return helper(root, 0)