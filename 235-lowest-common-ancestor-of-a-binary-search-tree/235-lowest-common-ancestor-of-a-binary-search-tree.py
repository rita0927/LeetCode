# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # O(logN) on average binary search tree or worst case O(N) for skewed tree
        # O(1) 
        
        cur = root
        
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
                
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
                
            else:
                return cur 
        
      
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         node = root
        
#         while node:
#             if p.val > node.val and q.val > node.val:
#                 node = node.right
#             elif p.val < node.val and q.val < node.val:
#                 node = node.left
#             else:
#                 return node
        