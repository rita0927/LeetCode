class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] 
        
        while len(dp) <= n:
            # additional "1" is added to the left of every bit in dp
            dp.extend([i + 1 for i in dp])
        # there will be more than n results in dp
        return dp[:n+1]
        
        
        
"""
digit   bits   dp
0		0000   [0]

1		0001   [0] extend [1] => [0,1]

2		0010   
3		0011   [0,1] extend [1,2] => [0,1,1,2]

4		0100
5		0101
6		0110
7		0111   [0,1,1,2] extend [1,2,2,3] => [0,1,1,2,1,2,2,3]

8		1000
9		1001
10		1010
11		1011
12		1100
13		1101
14		1110
15		1111   [0,1,1,2,1,2,2,3] extend [1,2,2,3,2,3,3,4] => [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4]

"""      
  
        
        
        
        
        
        
        
        
        
#         # O(nlogn), O(1)
#         def popCount(x):
#             count = 0
#             while x:
#                 if x & 1:
#                     count +=1
#                 x = x >>1
#             return count
   
#         dp = [0] * (n+1)
#         for i in range(n+1):
#             dp[i] = popCount(i)
#         return dp 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dp = [0] * (n + 1)

#         for i in range(n + 1):
#             dp[i] = dp[i // 2] + i % 2

#         return dp