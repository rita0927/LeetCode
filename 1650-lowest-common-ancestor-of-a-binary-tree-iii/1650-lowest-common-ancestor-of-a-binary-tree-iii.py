"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        parents= set()
        
        while p:
            parents.add(p)
            p = p.parent
        
        while q not in parents:
            q = q.parent
            
        return q 
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n1 = p 
#         n2 = q
        
#         while n1 != n2:
#             if n1:
#                 n1 = n1.parent
#             else:
#                 n1 = q
            
#             if n2:
#                 n2 = n2.parent
#             else:
#                 n2 = p
#         return n1 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         #O(m+n), O(1)
#         p_node = p
#         q_node = q
        
#         while p_node != q_node:
#             if p_node:
#                 p_node = p_node.parent
#             else:
#                 p_node = q
            
#             if q_node:
#                 q_node = q_node.parent
#             else:
#                 q_node = p
        
#         return p_node 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         parents = set()
        
#         while p:
#             parents.add(p)
#             p = p.parent
        
#         while q not in parents:
#             q = q.parent
        
#         return q 
        