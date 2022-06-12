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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None 
        
        queue= deque([root])
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                node = queue.popleft()
                
                if i < size - 1:
                    node.next = queue[0]
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root 
        
 
        
        

                
  
            
        
        



        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
  # O(N), O(1)      
        # # head and tail refers to the same dummy node, head record the path of the tail, used to retrieve the initial tail node
    
        # # can't set up the head/tail inside the while loop since they need to retain the value when node moves to the next in the same level (another while loop but the same level)
        
        # head = tail = Node()
        # node = root
        # while node:
        #     tail.next = node.left
        #     if tail.next:
        #         tail = tail.next 
        #     tail.next = node.right
        #     if tail.next:
        #         tail = tail.next
        #     node = node.next
        #     if not node:
        #   # move the tail pointer back to the beginning of the level
        #         tail = head
        #   # set the node to the next leftmost of the next level 
        #         node = head.next 
        # return root 

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# # O(N), O(N)
#         if not root:
#             return None
        
#         queue = deque([root])
        
#         while queue:
            
#             size = len(queue)
            
#             for i in range(size):
#                 node = queue.popleft()
                
#                 if i < size - 1:
#                     node.next = queue[0]
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#         return root 
                    
                
        