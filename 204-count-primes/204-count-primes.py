class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        dp = [1] * n
        dp[0] = dp[1] = 0
        
        for i in range(2,n):
            if dp[i]:
                for j in range(i*i, n, i):
                    dp[j] = 0
        return sum(dp)
        
        
        
        
        
        
        
        
      
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # Prime numbers: can only be divided by 1 and itself, 2,3,5,7,11... 
        
#         if n < 3:
#             return 0
        
#         lst = [1] * n
#         lst[0] = lst[1] = 0
#         for i in range(2,n):
#             if lst[i]:
#                 # numbers before i*i are alreay updated 
#                 for j in range(i*i, n, i):
#                     # j can be divided by i, so update the lst[j] to 0
#                     lst[j] = 0
#         return sum(lst)
        
        
        
        
        
        
        
        
      
        
        
        
#       if n < 3:
#         return 0

#       lst = [1] * n
#       lst[0] = lst[1] = 0

#       for i in range(2, n):
#         if lst[i]:
#           for j in range(i*i, n, i):
#             lst[j] = 0
#       return sum(lst)
        
        