"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None 
        
        d = {}
        
        node = head
        
        while node:
            d[node] = Node(node.val)
            node = node.next 
        
        node = head
        
        while node:
            new_node = d[node]
            new_node.next = d[node.next] if node.next else None
            new_node.random = d[node.random] if node.random else None 
            node = node.next 
            
        return d[head]
            
        

        

            
        
  

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
#         if not head:
#             return None
        
#         # Dictionary which holds old nodes as keys and new nodes as its values
#         dic = {}
        
#         node = head
        
#         # creat a new node for every node 
#         while node:
#             dic[node] = Node(node.val)
#             node = node.next
        
#         node = head
        
#         while node:
#             dic[node].next = dic[node.next] if node.next else None
#             dic[node].random = dic[node.random] if node.random else None
#             node = node.next
        
#         return dic[head]
        
        
        
        
        
        