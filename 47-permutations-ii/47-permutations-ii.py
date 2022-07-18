class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        count = Counter(nums)
        res = []
        
        def dfs(temp):
            if len(temp) == len(nums):
                res.append(temp.copy())
                return
            
            for n in count:
                if count[n]:
                    temp.append(n)
                    count[n] -= 1
                    dfs(temp)
                    temp.pop()
                    count[n] += 1
        dfs([])
        return res 
            
        


                    
                    
        

        
        

            
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
#         count = Counter(nums)
        
#         def dfs(perm):
#             if len(perm) == len(nums):
#                 res.append(perm.copy())
#                 return
            
#             for n in count:
#                 if count[n]:
#                     perm.append(n)
#                     count[n] -= 1
#                     dfs(perm)
#                     count[n] += 1
#                     perm.pop()
#         dfs([])
#         return res 
            
        

            
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
#         visited = set()
        
#         if len(nums) == 1:
#             return [nums.copy()]
        
#         for _ in range(len(nums)):
#             n = nums.pop(0)
            
#             if n not in visited:
#                 visited.add(n)
#                 perms = self.permuteUnique(nums)
                
#                 for perm in perms:
#                     perm.append(n)
#                 res.extend(perms)
#             nums.append(n)
              
#         return res 
        
        
       
        
        
        
#         res = []
        
#         def backtrack(perm, counter):
            
#             if len(perm) == len(nums):
#                 res.append(perm.copy())
#                 return
            
#             for num in counter:
#                 if counter[num]:
#                     perm.append(num)
#                     counter[num] -=1
#                     backtrack(perm, counter)
#                     perm.pop()
#                     counter[num] +=1
            
#         backtrack([], Counter(nums))
#         return res
        
