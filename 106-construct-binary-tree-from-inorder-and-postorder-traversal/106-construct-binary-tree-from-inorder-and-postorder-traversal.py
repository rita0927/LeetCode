# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def helper(l,r):
            if l > r:
                return None
            
            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            index = idx_map[root_val]
            root.right = helper(index + 1, r)
            root.left = helper(l, index - 1)
            
            
            
            return root
        
        idx_map = {}
        for i in range(len(inorder)):
            idx_map[inorder[i]] = i
        
        return helper(0, len(inorder) - 1)
        
        
        
        