"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]': 
        
        if not head:
            return None 
        
        def dfs(prev, node):
            
            if not node:
                return prev 
 
            node.prev= prev
            prev.next = node
            
            next = node.next 
            
            if node.child:
                child = node.child
                node.child = None
                node = dfs(node, child)
            if next:
                node = dfs(node, next)
            
            return node 
            
            # tail= dfs(node, node.child)
            # node.child = None
            # tail = dfs(tail, next) 
            # return tail  
        
        prev = dummy = Node()
        dfs(prev, head)
        dummy.next.prev = None
        return dummy.next 
                
                
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
#     # O(N), O(N)
#         if not head:
#             return None
#         # use dummy to hold the position of the start
#         prev = dummy = Node()
#         stack = [head]
        
#         while stack:
#             node = stack.pop()
#             prev.next = node
#             node.prev = prev
            
#             if node.next:
#                 stack.append(node.next)
#             if node.child:
#                 stack.append(node.child)
#                 node.child = None 
#             prev = node 
#         # detatch the dummy node from the head 
#         dummy.next.prev = None
#         return dummy.next 
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not head:
#             return None
        
#         cur = dummy = Node()
#         stack = [head]
        
#         while stack:
#             node = stack.pop()
            
#             if not node:
#                 return None
#             if node.next: stack.append(node.next)
#             if node.child: stack.append(node.child)
#             cur.next = node
#             node.prev = cur
#             node.child = None
#             cur = node 
#         dummy.next.prev = None 
#         return dummy.next 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not head:
#             return None 
        
#         cur = dummy = Node()
#         stack = [head]
        
#         while stack:
#             node = stack.pop()
            
#             if node.next:
#                 stack.append(node.next)
#             if node.child:
#                 stack.append(node.child)
#             cur.next = node
#             node.prev = cur
#             node.child = None
#             cur = node
#         dummy.next.prev = None
#         return dummy.next 
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
#         def dfs(node):
#             if not node:
#                 return None

#             next = node.next 
            
#             if node.child:
#                 node.next = dfs(node.child)
#                 node.child = None 
#             next.prev = node
#             node.next = dfs(next)
            
#             return node 
        
        return dfs(head)