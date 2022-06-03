# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None 
        
        res = []
        
        queue = deque([root])
        
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res 
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(N), O(h) where h is the height of the tree (recursion stack)
        
#         if not root:
#             return []
#         res = []
        
#         def bfs(node, level):
#             if level == len(res):
#                 res.append([])
            
#             res[level].append(node.val)
            
#             if node.left:
#                 bfs(node.left, level + 1)
#             if node.right:
#                 bfs(node.right, level + 1)
#         bfs(root, 0)
#         return res
            
        

                
                
                
        
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# O(N), O(N), space depends on the max number of nodes on a level. For a full tree, ignoring the constants, makes the space complexity of O(N)       
        
# must check None for root, otherwise it continues the while loop        
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
        