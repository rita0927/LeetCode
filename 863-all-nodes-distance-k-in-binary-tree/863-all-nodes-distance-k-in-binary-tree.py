# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        res = []
        
        def findParents(node, parent):
            if node:
                parents[node] = parent
                findParents(node.left, node)
                findParents(node.right, node)
        findParents(root, None)
        
        visited = set()
        def helper(node, dis):
            
            if node.val in visited:
                return 
            visited.add(node.val)
            
            if dis == k:
                res.append(node.val)
                return 
            
            for neighbor in [node.left, node.right, parents[node]]:
                if neighbor:
                    helper(neighbor, dis + 1)
        
        helper(target, 0)
        return res 
            
                
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
                