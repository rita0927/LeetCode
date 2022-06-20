class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = 0
        flips = 0
        for digit in s:
            if digit == '1':
                ones += 1
            else:
                flips += 1
            flips = min(flips, ones)
        return flips

                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         ones = 0
#         flips = 0
   
# # if we got 0 before 1, , all 0 or all 1, those are already monotonic inscreasing, no need to count
# # the count happends after encounting 1, then the flip happens (having 1 before 0)
#         for n in s:
#             # If we got a 1, go on. No need to flip. Just increment the 1 counter
#             if n == '1':
#                 ones += 1
#             # If we got a 0, we increment the flips counter.
#             if n == '0':
#                 flips += 1
#                 # Now we have two options. Either to flip the new zero to one or to flip all previous ones to zeros.
#             flips = min(flips, ones)
#         return flips 
        
        
        
 
        
        
#         # ETL O(n^2)

#         flipOne = 0
#         flipZero = 0
#         res = float('inf')
        
#         for i in range(1,len(s)):
#             flipOne = s[:i].count('1')
#             flipZero = s[i:].count('0')
#             res = min(res, flipOne + flipZero)
        
#         allZero = s.count('1')
#         allOne = s.count('0')
#         return min([allZero, allOne, res]) 
                
    
                
    
        
        
        
        
        
        
        
        
#         countOne = 0
#         flips = 0
        
#         for n in s:
#             if n == '1':
#                 countOne += 1
#             if n == '0':
#                 flips += 1
#             flips = min(countOne, flips)
        
#         return flips 
        
          
