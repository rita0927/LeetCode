# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 
            if slow == fast:
                return True 
        return False 

        

        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(n), O(1)
        
#         if not head:
#             return False
        
#         slow = head
#         fast = head.next
        
#         while fast and fast.next:
#             if slow == fast:
#                 return True
#             slow = slow.next
#             fast = fast.next.next
#         return False 
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         visited = set()
                        
#         while head:
#             if head not in visited:
#                 visited.add(head)
#                 head = head.next
#             else:
#                 return True
#         return False
        
        
        