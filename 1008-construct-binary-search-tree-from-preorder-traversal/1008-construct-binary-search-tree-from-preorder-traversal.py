# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def buildBST(node, val):
            if not node:
                return TreeNode(val)
            
            if val < node.val:
                node.left = buildBST(node.left, val)
            else:
                node.right = buildBST(node.right, val)
            return node 
        
        root = None
        for val in preorder:
            root = buildBST(root, val)
        return root 
        
        
        
#         def dfs(max_val):
#             if not preorder: return None
#             if not preorder[0] < max_val: return None
            
#             val = preorder.pop(0)
#             node = TreeNode(val)
#             node.left = dfs(val)
#             node.right = dfs(max_val)
            
#             return node
#         return dfs(float('inf'))
            