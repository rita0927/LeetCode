# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        visited = set()
        while head:
            if head not in visited:
                visited.add(head)
                head = head.next
            else:
                return head
        return None
                
        
        
        
        
        
        
        
        
#         if not head:
#             return head
        
#         index = 0
#         slow = head
#         fast = head.next
        
        