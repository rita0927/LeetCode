# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        vals = []
        cur = head
        
        while cur:
            vals.append(cur.val)
            cur = cur.next
            
        l = 0
        r = len(vals) - 1
        
        while l <= r:
            if vals[l] != vals[r]:
                return False
            l += 1
            r -= 1
        
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         val = []
#         cur = head
        
#         while cur:
#             val.append(cur.val)
#             cur = cur.next
#         return val == val[::-1]
        
       

        