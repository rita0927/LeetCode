# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast.next or not fast.next.next:
            return None
        
        fast = head
        
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return slow 
            
        
        
        
        
        
        
        
        
#         if not head:
#             return head
        
#         slow = head
#         fast = head
        
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next    
            
#             if slow == fast:
#                 slow = head
                
#                 while slow != fast:
#                     slow = slow.next
#                     fast = fast.next
#                 return slow

#         return None
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         visited = set()
#         while head:
#             if head not in visited:
#                 visited.add(head)
#                 head = head.next
#             else:
#                 return head
#         return None
                
        
        
        
        
        
        
        
        

        