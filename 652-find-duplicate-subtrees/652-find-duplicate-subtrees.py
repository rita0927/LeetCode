# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        res = []
        seen = defaultdict(int)
        
        def dfs(node):
            if not node:
                return 'N'
            path = f'{str(node.val)} {dfs(node.left)} {dfs(node.right)}'
            seen[path] += 1
            if seen[path] == 2:
                res.append(node)
            return path
        
        dfs(root)
        return res 