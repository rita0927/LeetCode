# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(l):
            prev = None        
            while l:
                next = l.next
                l.next = prev
                prev = l
                l = next
            return prev
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        head = None
        temp = 0
        while l1 or l2:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            temp = temp + val1 + val2
            
            cur = ListNode(temp%10)
            temp = temp //10
            cur.next = head
            head = cur
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if temp:
            cur = ListNode(temp)
            cur.next = head
            head = cur
        return head 
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def reverse(node):
#             prev = None
#             while node:
#                 next = node.next
#                 node.next = prev
#                 prev = node
#                 node = next
#             return prev
        
#         l1 = reverse(l1)
#         l2 = reverse(l2)
        
#         head = None
#         temp = 0
#         while l1 or l2:
#             val1 = l1.val if l1 else 0 
#             val2 = l2.val if l2 else 0
#             temp = temp + val1 + val2
            
#             cur = ListNode(temp%10)
#             cur.next = head
#             head = cur
#             temp = temp // 10
            
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
            
#         if temp:
#             cur = ListNode(temp)
#             cur.next = head
#             head = cur
#         return head 
            

            