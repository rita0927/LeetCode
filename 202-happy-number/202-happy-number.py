class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n not in seen:
            seen.add(n)
            cur = 0
            while n:
                n,remainder = divmod(n, 10)
                cur += remainder ** 2
            n = cur
        
        return n == 1 
        
        
            
                
                
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         seen = set()
        
#         remainder = n
        
#         while remainder not in seen:
#             seen.add(remainder)
#             cur = 0
#             while remainder:
#                 remainder, temp = divmod(remainder, 10)
#                 cur += temp ** 2
#             remainder = cur 
        
#         return remainder == 1 
        
        
        
        
        
        
        
        
        
        
        
        
        
      
        
        
        
        
        
        
        
        
#         seen = set()
        
#         while n != 1 and n not in seen:
#             seen.add(n)
#             temp = 0
            
#             while n:
#                 n, rem = divmod(n,10)
#                 temp += rem ** 2
#             n = temp 
            
#         return n == 1 

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(logn), O(logn)
        
#         seen = set()
        
#         while n not in seen:
#             seen.add(n)
#             temp = 0
#             while n:
#                 # temp += (n%10)**2
#                 temp += pow(n%10,2)
#                 n= n//10
#             n = temp
#         return n == 1
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         seen = set()
        
#         while n not in seen:
#             seen.add(n)
#             n = sum(int(d) ** 2 for d in str(n))
            
#         return n == 1
                
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#       seen = set()

#       while n not in seen:

#         seen.add(n)
#         n = sum(int(a)**2 for a in str(n))

#       return n == 1
        