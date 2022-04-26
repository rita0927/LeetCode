class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = defaultdict(int)
        res = 0
        
        for i in time:
            
            if i % 60 == 0:
                res += remainders[0]
            else:
                res += remainders[60 - i % 60]
                
            remainders[i % 60] +=1
        return res
           
        
        
        
    