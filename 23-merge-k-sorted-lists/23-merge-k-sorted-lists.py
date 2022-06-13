# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next 
        
        head = dummy = ListNode()
        
        while heap:
            val = heapq.heappop(heap)
            node = ListNode(val)
            head.next = node
            head = head.next 
        return dummy.next 


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(Nlogk) where N is the total nodes in the final LL, and k is the number of linked list. 
#         # O(k) + O(n). Heap only store k elements, O(n) for creating the new LL
        
        
#         head = dummy = ListNode()
#         heap = []
        
#         for l in lists:
#             while l:
#                 heapq.heappush(heap, l.val)
#                 l = l.next
                
#         while heap:
#             dummy.next = ListNode(heapq.heappop(heap))
#             dummy = dummy.next
#         return head.next 
        
        
        
                    
                    
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(NlogN) N is the total number of nodes, O(N)
#         lst = []
        
#         for l in lists:
#             while l:
#                 lst.append(l.val)
#                 l = l.next
#         lst.sort()   
#         head = dummy = ListNode()
        
#         for val in lst:
#             dummy.next = ListNode(val)
#             dummy = dummy.next
            
#         return head.next 
        
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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





        
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        