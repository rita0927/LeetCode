# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        

# O(N), O(N) due to the call stack
        def helper(node):
            if not node:
                return None
            elif node.val < low:
                return helper(node.right)
            elif node.val > high:
                return helper(node.left)
            else:
                node.left = helper(node.left)
                node.right = helper(node.right)
                return node 
        
        return helper(root)
        