# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parents = {}
        start = None 
        
        queue = deque([(root, None)])
        while queue:
            node, parent = queue.popleft()
            parents[node] = parent
            
            if node.val == startValue:
                start = node
            
            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))
        
        queue = deque([(start, '')])
        visited = set()
        
        while queue:
            node, path = queue.popleft()
            
            if node.val in visited:
                continue 
            visited.add(node.val)
            
            if node.val == destValue:
                return path 
            
            if node.left:
                queue.append((node.left, path+'L'))
            if node.right:
                queue.append((node.right, path+'R'))
            if parents[node]:
                queue.append((parents[node], path +'U'))
            
            
            
            
        
            
            
            
        

                
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         parents = {}
#         self.start = None 
#         def findParent(parent, node):
#             parents[node] = parent
#             if node.val == startValue:
#                 self.start = node
            
#             if node.left:
#                 findParent(node, node.left)
#             if node.right:
#                 findParent(node, node.right)
#         findParent(None, root)
        
#         queue = deque([(self.start, '')])
#         visited = set()
        
#         while queue:
#             node, path = queue.popleft()
            
#             if node.val in visited:
#                 continue
#             visited.add(node.val)
            
#             if node.val == destValue:
#                 return path 
            
#             if node.left and node.left.val not in visited:
#                 queue.append((node.left, path+'L'))
#             if node.right and node.right.val not in visited:
#                 queue.append((node.right, path+'R'))
#             if parents[node] and parents[node].val not in visited:
#                 queue.append((parents[node], path+'U'))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         #O(N), O(N)
#         graph = defaultdict(list)
#         queue = deque([root])
        
#         while queue:
#             node = queue.popleft()
#             if node.left:
#                 graph[node.val].append([node.left.val, 'L'])
#                 graph[node.left.val].append([node.val, 'U'])
#                 queue.append(node.left)
#             if node.right:
#                 graph[node.val].append([node.right.val, 'R'])
#                 graph[node.right.val].append([node.val, 'U'])
#                 queue.append(node.right)
        
#         queue = deque([(startValue, '')])
#         visited = set()
#         visited.add(startValue)
#         while queue:
#             val, path = queue.popleft()
            
#             if val == destValue:
#                 return path
            
#             for next, dir in graph[val]:
#                 if next not in visited:
#                     visited.add(next)
#                     queue.append((next, path+dir))
                
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         parents = {}
#         self.start = None

#         def findNode(parent, node):

#             parents[node] = parent
#             if node.val == startValue:
#                 self.start = node
            
#             if node.left:
#                 findNode(node, node.left)
#             if node.right:
#                 findNode(node, node.right)
            
#         findNode(None, root)
#         queue = deque([(self.start, '')])
#         visited = set()
#         visited.add(self.start.val)
        
#         while queue:

#             node, path = queue.popleft()
            
#             if node.val == destValue:
#                 return path
#             if node.left and node.left.val not in visited:
#                 queue.append((node.left, path+'L'))
#                 visited.add(node.left.val)
#             if node.right and node.right.val not in visited:
#                 queue.append((node.right, path+'R'))
#                 visited.add(node.right.val)
#             if parents[node] and parents[node].val not in visited:
#                 queue.append((parents[node], path+'U'))
#                 visited.add(parents[node].val)
                    
        
                        