class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        ones = sum(data)
        if ones <= 1:
            return 0
        
        maxOnes = 0
        l = 0
        curOnes = 0
        for r in range(len(data)):
            curOnes += data[r]
            
            if r-l+1 == ones:
                maxOnes = max(maxOnes, curOnes)   
                curOnes -= data[l]
                l += 1
        return ones - maxOnes 
        