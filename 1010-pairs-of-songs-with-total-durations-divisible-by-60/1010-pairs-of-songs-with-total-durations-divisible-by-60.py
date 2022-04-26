class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = {}
        res = 0
        
        for i in range(len(time)):
            remainder = 60 - time[i] % 60

            if remainder in remainders:
                res +=remainders[remainder]
            elif remainder == 60 and 0 in remainders:
                res += remainders[0] 
                    
            remainders[time[i] % 60] = remainders.get(time[i] % 60, 0) + 1
            
        return res
        