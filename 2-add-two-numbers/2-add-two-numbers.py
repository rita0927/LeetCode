# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = head = ListNode()
        carry = 0
        
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = carry + val1 + val2
            dummy.next = ListNode(val%10)
            dummy = dummy.next 
            carry = val//10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 
        
        if carry:
            dummy.next = ListNode(carry)
        
        return head.next 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dummy = head = ListNode()
#         carry = 0
#         while l1 or l2:
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0
            
#             val = (val1 + val2 + carry)%10
#             node = ListNode(val)
#             carry = (val1 + val2 + carry)//10
#             head.next = node
#             head = node 
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None 
        
#         if carry:
#             node = ListNode(carry)
#             head.next = node
            
#         return dummy.next 
            
        
        
        
        
        
        
        
        
#         # def reverseList(head):
#         #     prev = ListNode()
#         #     while head:
#         #         next = head.next
#         #         head.next = prev
#         #         prev = head 
#         #         head = next 
#         #     return prev 
        
#         def convertToArr(head):
#             arr = []
#             while head:
#                 arr.append(head.val)
#                 head = head.next 
#             return arr
#         arr1 = convertToArr(l1)
#         arr2 = convertToArr(l2)
        
#         res = []
#         remainder = 0
#         i = -1
#         length = max(len(arr1), len(arr2))
        
#         while i>=-length:
#             val1 = arr1[i] if arr1[i] else 0
#             val2 = arr2[i] if arr2[i] else 0
            
#             res.append((val1 + val2 + remainder) % 10)
#             remainder = (val1 + val2)//10
#             i -= 1
#         if remainder:
#             res.append(remainder)
        
#         dummy = head = ListNode()
#         i = 0
#         while i < len(res):
#             node = ListNode(res[i])
#             dummy.next = node
#             dummy = node
#             i += 1
        
#         return head.next 
            
            
            
            
            
            
                
                
                
        