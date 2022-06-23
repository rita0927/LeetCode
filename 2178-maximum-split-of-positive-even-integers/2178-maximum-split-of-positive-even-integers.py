class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        
        res = set()
        
        if finalSum %2:
            return []
        
        num = 2
        
        while finalSum >0:
            res.add(num)
            finalSum -= num
            num += 2
            
            if finalSum < 0:
                res.remove(-finalSum)
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = set()
        
#         if finalSum % 2:
#             return []
        
#         num = 2
        
#         while finalSum >0:
#             res.add(num)
#             finalSum -= num
#             num += 2
            
#             if finalSum <0:
#                 res.remove(-finalSum)
#                 break
#         return res 
                
            

        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
        
#         if finalSum % 2 or finalSum < 2:
#             return []
        
#         cur_sum = 0
#         cur_num = 2

#         while cur_sum < finalSum:
#             res.append(cur_num)
#             cur_sum += cur_num
#             cur_num +=2
        
#         if cur_sum == finalSum:
#             return res 
#         else:
#             # res.remove(cur_sum - finalSum)
#             res.pop(res.index(cur_sum-finalSum))
        
#         return res 
        