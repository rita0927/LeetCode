class Solution:
    def hammingWeight(self, n: int) -> int:
        
        res = 0
        
        while n:
            if n & 1:
                res += 1
            n = n >> 1
        return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = 0
        
#         while n:
#             if n & 1:
#                 res +=1
#             n = n >> 1
#         return res 
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # ones = 0
        # while (n != 0):
        #     ones= ones+(n & 1)
        #     n= n >> 1
        # return ones