# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def convertToString(node):
            if not node:
                return 'N'
            
            return f'#{node.val} {convertToString(node.left)} {convertToString(node.right)}'
        
        return convertToString(subRoot) in convertToString(root)
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
#         def helper(root1, root2):
#             if not root1 and not root2:
#                 return True
#             if not root1 or not root2 or root1.val != root2.val:
#                 return False
#             else:
#                 return helper(root1.left, root2.left) and helper(root1.right, root2.right)
            
        
#         def dfs(node):
#             if node:
#                 if node.val == subRoot.val:
#                     if helper(node, subRoot):
#                         return True
#                 return dfs(node.left) or dfs(node.right)
            
#         return dfs(root)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def convertToString(node):
#             if node:
#                 # use the "#" as a deliminator, example case  [12], [2] 
#                 return f"#{node.val} {convertToString(node.left)} {convertToString(node.right)}"
        
#         return convertToString(subRoot) in convertToString(root)
        
        
        
        
        
        
        
        
        
        
        
        
   
        
#         def dfs(root, subRoot):
            
#             if not root and not subRoot:
#                 return True
#             elif not root or not subRoot or root.val != subRoot.val:
#                 return False
#             else:
#                 return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)
        
#         queue = deque([root])
        
#         while queue:
#             node = queue.popleft()
#             if node.val == subRoot.val:
#                 if dfs(node, subRoot):
#                     return True
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         return False 
            
            
        
        

            
                