class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        ones = sum(data)
        maxOnes = 0
        curOnes = 0
        l = 0
        
        for r in range(len(data)):
            curOnes += data[r]
            
            if r-l+1 == ones:
                maxOnes = max(maxOnes, curOnes)
                curOnes -= data[l]
                l+= 1
        return ones - maxOnes 
                
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(N), O(1)
#         # count the ones in the data, which is also the width of the window 
#         ones = sum(data)
#         # optional: if there's only one 1, no need to swamp
#         if ones <= 1:
#             return 0
        
#         # track the max amount of ones within a window
#         maxOnes = 0
#         l = 0
#         # num of ones in current window 
#         curOnes = 0
#         for r in range(len(data)):
#             curOnes += data[r]
#             # when the window reaches the full width 
#             if r-l+1 == ones:
#                 maxOnes = max(maxOnes, curOnes)   
#                 curOnes -= data[l]
#                 l += 1
#         # total num of ones minus the max ones within a window
#         return ones - maxOnes 
        