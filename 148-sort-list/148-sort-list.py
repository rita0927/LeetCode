# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head 
        
        def merge(l1,l2):
            dummy = cur = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = ListNode(l1.val)
                    l1 = l1.next 
                else:
                    cur.next = ListNode(l2.val)
                    l2 = l2.next 
                cur = cur.next 
            cur.next = l1 if l1 else l2
            return dummy.next 
         
        slow = head
        fast = head.next 
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 
        l2 = slow.next 
        l1 = head 
        slow.next = None 
        
        return merge(self.sortList(l1), self.sortList(l2))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#        # O(nlogn) for two phases, including split O(logn) and merge O(n)
#        # O(logn) due to the call stack      

#         if not head or not head.next:
#             return head 
        
#         def merge(l1, l2):
#             dummy = cur = ListNode()
#             while l1 and l2:
#                 if l1.val < l2.val:
#                     cur.next = ListNode(l1.val)
#                     l1 = l1.next 
#                 else:
#                     cur.next = ListNode(l2.val)
#                     l2 = l2.next 
#                 cur = cur.next 
#             cur.next = l1 if l1 else l2 
#             return dummy.next 
        
#         slow = head 
#         fast = head.next 
#         while fast and fast.next:
#             fast = fast.next.next 
#             slow = slow.next 
#         l2 = slow.next 
#         l1 = head
#         slow.next = None 
        
#         return merge(self.sortList(l1), self.sortList(l2))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not head or not head.next:
#             return head 
    
#         def getMid(head):
            
#             # can't set both slow & fast as head, otherwise, the last two nodes always stick in left/head
#             # slow refers to the last node in the left, node the starting node of right
#             slow = head
#             fast = head.next
#             while fast and fast.next:
#                 fast = fast.next.next
#                 slow = slow.next
#             return slow 
          
#         def merge(l1, l2):
#             dummy = cur = ListNode()
#             while l1 and l2:
#                 if l1.val < l2.val:
#                     cur.next = ListNode(l1.val)
#                     l1 = l1.next 
#                 else:
#                     cur.next = ListNode(l2.val)
#                     l2 = l2.next 
#                 cur = cur.next 
#             cur.next = l1 if l1 else l2 
#             return dummy.next 
        
#         l1 = head
#         # mid is the last node in the l1/left
#         mid = getMid(head)
#         # mid.next is the starting node of l2/right
#         l2 = mid.next
#         # cut off the link between l1 & l2 
#         mid.next = None 
        
#         l1 = self.sortList(l1)
#         l2 = self.sortList(l2)
#         return merge(l1, l2)


            
        
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if not head or not head.next:
#             return head
        
#         left = head
#         right = self.getMid(head)
#         temp = right.next
#         right.next = None
#         right = temp
        
#         left = self.sortList(left)
#         right = self.sortList(right)
#         return self.mergeList(left, right)
    
#     def getMid(self, head):
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow
    
#     def mergeList(self, left, right):
#         tail = dummy = ListNode()
        
#         while left and right:
#             if left.val < right.val:
#                 tail.next = left
#                 left = left.next
#             else:
#                 tail.next = right
#                 right = right.next
#             tail = tail.next
#         if left: 
#             tail.next = left
#         if right:
#             tail.next = right
            
#         return dummy.next 
    
        
        
        
        
        
        
     
        
        
        
        
        
        
        
        
        
        
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
        