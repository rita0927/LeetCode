# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        res = []
        d = defaultdict(int)
        def dfs(node):
            if not node:
                return 'N'
            
            path = f'{str(node.val)} {dfs(node.left)} {dfs(node.right)}'
            d[path] += 1
            if d[path] == 2:
                res.append(node)
            return path 
        
        dfs(root)
        return res 




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


        
        
        
        
        
        
        
        
        
        
        
        
#         # either res or seen can be set
#         # each node are considered different in set
#         # seen is used to count the occurance of the same path
#         res = []
#         seen = defaultdict(int)
        
#         def dfs(node):
#             if not node:
#                 # None can be marked by any non-digit, including empty string
#                 return 'N'
#             path = f'{str(node.val)} {dfs(node.left)} {dfs(node.right)}'
#             seen[path] += 1
#             # can't use set because same path may be more than 2
#             if seen[path] == 2:
#                 res.append(node)
#             return path
        
#         dfs(root)
#         return res 