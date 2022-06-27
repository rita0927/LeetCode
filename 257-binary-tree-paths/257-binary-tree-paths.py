# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        res = []
        def helper(node, path):
            path += str(node.val)
            
            if not node.left and not node.right:
                res.append(path)
                return
            
            if node.left:
                helper(node.left, path+'->')
            if node.right:
                helper(node.right, path+'->')
        
        helper(root, '')
        
        return res
                
        