# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root or root == p or root == q:
            return root 
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        
        if l and r:
            return root
        elif l:
            return l
        else:
            return r 
        
        

  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not root or root == p or root == q:
#             return root
        
#         l = self.lowestCommonAncestor(root.left, p, q)
#         r = self.lowestCommonAncestor(root.right, p, q)
        
#         if l and r:
#             return root
#         elif l:
#             return l
#         else:
#             return r
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # find parents
#         stack = [root]
#         parent = {root: None}
        
#         while p not in parent or q not in parent:
#             node = stack.pop()
            
#             if node.left:
#                 stack.append(node.left)
#                 parent[node.left] = node
#             if node.right:
#                 stack.append(node.right)
#                 parent[node.right] = node   
                
#         # find ancestors 
        
#         # use set to save time looking for q, time complexity is O(1)
#         # list works as well but time complexity increases to O(n)
#         ancestors = set()
#         while p:
#             ancestors.add(p)
#             p = parent[p]
        
#         # common ancestor
#         while q not in ancestors:
#             q = parent[q]
            
#         return q
        
        
        
     
        
        
        
#         # base case
#         if not root or root == p or root == q:
#             return root 
        
#         # recursion 
#         left = self.lowestCommonAncestor(root.left, p, q)
#         right = self.lowestCommonAncestor(root.right, p, q)

#         # return 

#         if left and right:
#             return root
        
#         return left if left else right 
        
        
        
        
     
        