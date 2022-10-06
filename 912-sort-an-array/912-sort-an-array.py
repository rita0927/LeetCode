class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def helper(l,r):
            l_index=0
            r_index=0
            res=[]
            while l_index<len(l) and r_index<len(r):
                if l[l_index]<r[r_index]:
                    res.append(l[l_index])
                    l_index+=1
                else:
                    res.append(r[r_index])
                    r_index+=1
            res.extend(l[l_index:])
            res.extend(r[r_index:])
            return res 

        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        l=self.sortArray(nums[:mid])
        r=self.sortArray(nums[mid:])
        return helper(l,r)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def helper(l,r):
#             res = []
#             l_idx = 0
#             r_idx = 0
#             while l_idx < len(l) and r_idx < len(r):
#                 if l[l_idx] < r[r_idx]:
#                     res.append(l[l_idx])
#                     l_idx += 1
#                 else:
#                     res.append(r[r_idx])
#                     r_idx += 1
#             res.extend(l[l_idx:])
#             res.extend(r[r_idx:])
            
#             return res 
            
#         if len(nums) <= 1:
#             return nums 
        
#         mid = len(nums)//2
#         l = self.sortArray(nums[:mid])
#         r = self.sortArray(nums[mid:])
#         return helper(l,r)
    
        
         
