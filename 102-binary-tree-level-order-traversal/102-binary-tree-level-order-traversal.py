# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = deque([root])
        res = []
        temp = []
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                temp.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
            temp = []
        return res 
        

                
                
                
        
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not root:
#             return []

#         queue = deque([root])
#         temp = []
#         res = []

#         while queue:
#             level_size = len(queue)
#             for _ in range(level_size):
#                 node = queue.popleft()
#                 temp.append(node.val)

#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             res.append(temp)
#             temp = []

#         return res
        