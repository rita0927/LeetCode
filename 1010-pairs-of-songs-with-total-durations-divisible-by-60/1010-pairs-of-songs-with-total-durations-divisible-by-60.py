class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = defaultdict(int)
        res = 0
        for t in time:
            complement = 60 - t%60
            
            if complement in dic:
                res += dic[complement]
            
            if not t%60:
                res +=dic[0]
            
            dic[t%60] +=1
            
        return res 
                
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         remainders = defaultdict(int)
#         res = 0
        
#         for i in time:
            
#             if i % 60 == 0:
#                 res += remainders[0]
#             else:
#                 res += remainders[60 - i % 60]
                
#             remainders[i % 60] +=1
#         return res
           
        
        
        
    