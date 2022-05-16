# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        lst = []
        
        for l in lists:
            while l:
                lst.append(l.val)
                l = l.next
        lst.sort()   
        head = dummy = ListNode()
        
        for val in lst:
            head.next = ListNode(val)
            head = head.next
            
        return dummy.next 
        
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         heap = []
        
#         for l in lists:
#             while l: 
#                 heappush(heap, l.val)
#                 l = l.next
                
#         dummy = node = ListNode()
        
#         while heap:
#             node.next = ListNode(heappop(heap))
#             node = node.next
        
#         return dummy.next 
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         heap = []
#         for l in lists:
#             while l:
#                 heappush(heap, l.val)
#                 l = l.next
        
#         dummy = node = ListNode()
        
#         while heap:
#             node.next = ListNode(heappop(heap))
#             node = node.next
            
#         return dummy.next 
            
        
# Time: O(Nlogk)
# Space: 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         arr = []
#         for l in lists:
#             while l:
#                 arr.append(l.val)
#                 l=l.next
        
#         dummy = node = ListNode()
        
#         for i in sorted(arr):
#             node.next = ListNode(i)
#             node = node.next
        
#         return dummy.next 
        
        
# # O(NlogN), O(N), N is the total number of nodes 





        
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        