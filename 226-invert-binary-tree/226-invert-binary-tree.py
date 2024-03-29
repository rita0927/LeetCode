# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            node.left, node.right = node.right, node.left
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        return root 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not root:
#             return root
        
        
#         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        
#         return root
        
        
        
        
        

    
        
        
#         if not root:
#             return None
        
#         stack = [root]
        
#         while stack:
#             node = stack.pop()
#             if node:
#                 temp = node.left
#                 node.left = node.right
#                 node.right = temp
            
#                 stack.append(node.left)
#                 stack.append(node.right)
                
#         return root
            
            
        
        
   
        
        
#         if not root:
#             return None
        
#         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
#         # right = self.invertTree(root.right)
#         # left = self.invertTree(root.left)
#         # root.right = left
#         # root.left = right
#         return root 

