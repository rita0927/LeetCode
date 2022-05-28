# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        
        def findParent(node, parent):
            node.parent = parent
            if node.left:
                findParent(node.left, node)
            if node.right:
                findParent(node.right, node)
        findParent(root, None)
        
        res = []
        visited = set()
        queue = deque([(target, 0)])
        
        while queue:
            node, distance = queue.popleft()
            visited.add(node)
            
            if distance == k:
                res.append(node.val)
                continue
            for next in [node.left, node.right, node.parent]:
                if next and next not in visited:
                    queue.append((next, distance+1))
        return res 
        
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         parents = {}
#         res = []
        
#         def findParents (node, parent):
#             if node:
#                 parents[node] = parent
#                 findParents(node.left, node)
#                 findParents(node.right, node)
#         findParents(root, None)
        
#         queue = deque([(target, 0)])
#         visited = set()
#         visited.add(target.val)
#         while queue: 
#             node, dis = queue.popleft()
#             if dis == k:
#                 res.append(node.val)
#                 continue
            
#             for neighbor in [node.left, node.right, parents[node]]:
#                 if neighbor and neighbor.val not in visited:
#                     visited.add(neighbor.val)
#                     queue.append((neighbor, dis + 1))
#         return res 
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         parents = {}
#         res = []
        
#         def findParents(node, parent):
#             if node:
#                 parents[node] = parent
#                 findParents(node.left, node)
#                 findParents(node.right, node)
#         findParents(root, None)
        
#         visited = set()
#         def helper(node, dis):
            
#             if node.val in visited:
#                 return 
#             visited.add(node.val)
            
#             if dis == k:
#                 res.append(node.val)
#                 return 
            
#             for neighbor in [node.left, node.right, parents[node]]:
#                 if neighbor:
#                     helper(neighbor, dis + 1)
        
#         helper(target, 0)
#         return res 
            
                
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
#         parents = {}
        
#         def findParent(node, parent):
#             if node:
#                 parents[node] = parent
#                 findParent(node.left, node)
#                 findParent(node.right, node)
            
#         findParent(root, None)
        
        
#         visited = set()
        
#         def helper(node, distance):
            
#             if not node or distance > k:
#                 return
            
#             if node.val in visited:
#                 return 
            
#             visited.add(node.val)
            
#             if distance == k:
#                 res.append(node.val)
            
#             for neightbor in [node.left, node.right, parents[node]]:
#                 helper(neightbor, distance + 1)
        
#         helper(target, 0)
        
#         return res
                
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
        
#         parents = {}
        
#         def findParent(node, parent):
#             if node:
#                 parents[node] = parent
#                 findParent(node.left, node)
#                 findParent(node.right, node)
                
#         findParent(root, None)
        
#         visited = set()
        
#         def search(node, distance):
            
#             if not node or node.val in visited:
#                 return 
#             visited.add(node.val)

#             if distance == k :
#                 res.append(node.val)

#             for neighbor in [parents[node], node.left, node.right]:
#                 search(neighbor, distance + 1)
      
#         search(target, 0)       
   
#         return res
                