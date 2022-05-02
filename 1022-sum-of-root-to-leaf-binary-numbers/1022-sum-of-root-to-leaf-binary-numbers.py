# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        
        def helper(node, subtotal):
            if node:
                subtotal = subtotal<< 1 | node.val
            
                if not node.left and not node.right:
                    self.total += subtotal

                helper(node.left, subtotal)
                helper(node.right, subtotal)
        
        helper(root, 0)
        return self.total
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
       
#         self.total = 0
#         stack =[(root, 0)]
        
#         while stack:
#             node, subtotal = stack.pop()
            
#             if node:
#                 # subtotal = subtotal << 1 | node.val
#                 subtotal = subtotal * 2 + node.val
            
#                 if not node.left and not node.right:
#                     self.total += subtotal
#                     continue
                
#                 stack.append((node.left, subtotal))
#                 stack.append((node.right, subtotal))
            
#         return self.total
                
    
        
        
        
        
        
        
        
        
        
        
#         self.total = 0
        
#         def helper(node, subtotal):
            
#             if node:
#                 subtotal = subtotal << 1 | node.val
            
#             # Add to the total when both the left and right are null
#             # Otherwise the subtotal will be added twice
            
#             if not node.left and not node.right:
#                 self.total += subtotal
#                 return
#             helper(node.left, subtotal)
#             helper(node.right, subtotal)
            
#         helper(root, 0)
#         return self.total

            
            