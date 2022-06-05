"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        if not root:
            return None
        
        node = root
        next = node.left
        
        while next:
            node.left.next = node.right
            
            if node.next:
                node.right.next = node.next.left
                node = node.next 
                
            else:
                node = next
                next = node.left 
        
        return root 
        
        
        
        
        
        
        
        
        
        
        
#         if not root:
#             return None
        
#         node = root
#         # next is the first node in the next level
#         next= node.left
        
#         # while the next level exists
#         while next:
#             # when the next level exists, build the connection between two child nodes
#             node.left.next = node.right
#             # there're node after at the same level
#             if node.next:
#                 node.right.next = node.next.left
#                 node = node.next
#             # last node at this level
#             else:
#                 node = next
#             # set the next as the first node in the next level
#                 next = node.left
             
#         return root 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not root:
#             return None
#         cur = root
#         next = root.left

#         while next:
#             cur.left.next = cur.right
#             if cur.next:
#                 cur.right.next = cur.next.left
#                 cur = cur.next
#             else:
#                 cur = next
#                 next = cur.left
#         return root  
        