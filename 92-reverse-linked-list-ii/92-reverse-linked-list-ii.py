# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
#         if left == right:
#             return head 
        
        dummy = prev = ListNode(0, head)
        cur = head 
        pos = 1
        
        while pos < left:
            prev = cur
            cur = cur.next 
            pos += 1
            
        l = prev 
        
        while pos - 1 < right:
            nxt = cur.next 
            cur.next = prev
            prev = cur
            cur = nxt    
            pos += 1
        
        nxt = l.next 
        l.next = prev
        nxt.next = cur 
        
        return dummy.next 
        
        
        
        
        
        
        
        
        
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if left == right:
#             return head 
        
#         # dummy.next refers to the head 
#         dummy = prev = ListNode(0, head)
#         # position starting from 1
#         i = 1
        
#         # find the node before left, mark with prev 
#         while i < left:
#             prev = prev.next 
#             i += 1
        
#         # prev is the node before the left, prev.next -> left (starting reverse)
#         cur = prev.next 
#         next = cur.next 
        
#         # when i == right: 
#         #    cur -> right, need to connect with prev (node before left)
#         #    next -> node after right, need to connect with left
#         while i < right:
#             temp = next.next 
#             next.next = cur
#             cur = next 
#             next = temp
#             i += 1
        
#         # left (initial prev.next) connects to the node after right 
#         prev.next.next = next 
#         # prev connects to the right (ending cur)
#         prev.next = cur 
        
#         # dummy refers to the node before head 
#         return dummy.next 
        

        