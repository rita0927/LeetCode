# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        idx_map = {}
        
        for index, val in enumerate(inorder):
            idx_map[val] = index
            
        def helper(l,r):
            if l > r:
                return None
            val = preorder.pop(0)
            root_idx = idx_map[val]
            root = TreeNode(val)
            
            root.left = helper(l, root_idx - 1)
            root.right = helper(root_idx + 1, r)
            
            return root
        
        return helper(0, len(inorder) - 1)