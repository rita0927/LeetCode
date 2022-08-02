# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        res = []
        
        queue = deque()
        queue.append([root, 0])
        
        while queue:
            node, level = queue.popleft()

            if len(res) == level:
                res.append(deque())
            
            if level%2:
                res[level].appendleft(node.val)
            else:
                res[level].append(node.val)
            
            if node.left:
                queue.append([node.left, level+1])
            if node.right:
                queue.append([node.right, level+1])
        return res 
                

            
            
            
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(N), O(N)       
        
#         if not root:
#             return []
        
#         res = []
#         queue = deque([(root, 0)])
        
#         while queue:
#             level_size = len(queue)
#             temp = deque()
#             for _ in range(level_size):
#                 node, level = queue.popleft()
                
#                 if level % 2:
#                     temp.appendleft(node.val)
#                 else:
#                     temp.append(node.val)
                
#                 if node.left:
#                     queue.append((node.left, level+ 1))
#                 if node.right:
#                     queue.append((node.right, level + 1))
#             res.append(temp)
#         return res 
        
        
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(N), O(H)
        
#         if not root:
#             return []
        
#         res = []
        
#         def dfs(node, level):
#             if len(res) == level:
#                 res.append(deque())
            
#             if level%2:
#                 res[level].appendleft(node.val)    
#             else:
#                 res[level].append(node.val)
            
#             if node.left:
#                 dfs(node.left, level + 1)
#             if node.right:
#                 dfs(node.right, level + 1)
#         dfs(root, 0)
#         return res 
                
                
                
                
             
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

                
        
        
        