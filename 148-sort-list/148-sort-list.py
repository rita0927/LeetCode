# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next = None
        right = temp
        
        left = self.sortList(left)
        right = self.sortList(right)
        return self.mergeList(left, right)
    
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def mergeList(self, left, right):
        tail = dummy = ListNode()
        
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left: 
            tail.next = left
        if right:
            tail.next = right
            
        return dummy.next 
    
        
        
        
        
        
        
     
        
        
        
        
        
        
        
        
        
        
#         if not head or not head.next:
#             return head
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         mid = slow.next
#         slow.next = None
#         left = self.sortList(head)
#         right = self.sortList(mid)

#         return self.merge(left, right)

#     def merge(self, l, r):
#         if not l or not r:
#             return l or r

#         dummy = cur = ListNode(0)

#         while l and r:
#             if l.val < r.val:
#                 cur.next = l
#                 l = l.next
#             else:
#                 cur.next = r
#                 r = r.next
#             cur = cur.next
#         # if any nodes left in l or r, cur.next will link to the remaining
#         cur.next = l or r

#         return dummy.next
        