# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = defaultdict(list)
        
        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            level = max(left, right) + 1
            res[level].append(node.val)
            return level 
        dfs(root)
        return res.values()
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         leaves = defaultdict(list)

#         def dfs(node):
            
#             if not node:
#                 return -1
            
#             left = dfs(node.left)
#             right = dfs(node.right)
#             height = max(left, right) + 1
#             leaves[height].append(node.val)
            
#             return height
        
#         dfs(root)
        
#         # Dicts preserve insertion order 
#         return leaves.values()
            
            

        