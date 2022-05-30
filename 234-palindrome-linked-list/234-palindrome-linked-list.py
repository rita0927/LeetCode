# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev= None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        
        left, right = head, prev
        
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         #O(N), O(N)        
        
#         vals = []
#         cur = head
        
#         while cur:
#             vals.append(cur.val)
#             cur = cur.next
            
#         l = 0
#         r = len(vals) - 1
        
#         while l <= r:
#             if vals[l] != vals[r]:
#                 return False
#             l += 1
#             r -= 1
        
#         return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         val = []
#         cur = head
        
#         while cur:
#             val.append(cur.val)
#             cur = cur.next
#         return val == val[::-1]
        
       

        