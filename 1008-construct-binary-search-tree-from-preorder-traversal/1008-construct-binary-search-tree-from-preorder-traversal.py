# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def helper(max_val):
            if not preorder:
                return None 
            
            if preorder[0] > max_val:
                return None 
            
            val = preorder.pop(0)
            node = TreeNode(val)
            node.left = helper(val)
            node.right = helper(max_val)
            
            return node 
        return helper(float("inf"))
            
        
                                                               
                                                               
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def helper(max_val):
#             # if all elements from preorder are used
#             # the tree is constructed
#             if not preorder: return None
#             if preorder[0] >= max_val: return None
            
#             val = preorder.pop(0)
#             node = TreeNode(val)
#             node.left = helper(val)
#             node.right = helper(max_val)
#             return node
        
#         # going left first by default tree traversal pattern (preorder),  guaranteed to have placed the least element first. only need to check the upper limit.

#         return helper(float('inf'))
            
        


        
        
        
        
        
        
        
        
        
        
        
        
#         # O(N^2)
#         def buildBST(node, val):
#             if not node:
#                 return TreeNode(val)
            
#             if val < node.val:
#                 node.left = buildBST(node.left, val)
#             else:
#                 node.right = buildBST(node.right, val)
#             return node 
        
#         root = None
#         for val in preorder:
#             root = buildBST(root, val)
#         return root 
        
        
        
#         def dfs(max_val):
#             if not preorder: return None
#             if not preorder[0] < max_val: return None
            
#             val = preorder.pop(0)
#             node = TreeNode(val)
#             node.left = dfs(val)
#             node.right = dfs(max_val)
            
#             return node
#         return dfs(float('inf'))
            