class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if x == 0:
            return 0
        
        def helper(num, power):
            if not power:
                return 1
            
            temp = helper(num, power//2) 
            temp = temp * temp
            return temp * num if power%2 else temp
        res = helper(x,abs(n))
        return  res if n > 0 else 1/helper(x, abs(n))
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def helper(x, n):
#             if x == 0:
#                 return 0
#             if n == 0:
#                 return 1

#             res = helper(x, n // 2)
#             res *= res
#             return x * res if n % 2 else res

#         res = helper(x, abs(n))
#         return res if n >= 0 else 1 / res
    
    
    
#         if n < 0:
#             x = 1 / x
#             n=-n

#         ans = 1
#         tmp = x
#         while n != 0:
#             if n % 2 == 1:
#                 ans *= tmp
#             tmp *= tmp
#             n = n// 2
#         return ans
