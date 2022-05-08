class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def backtrack(perm, counter):
            
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for num in counter:
                if counter[num]:
                    perm.append(num)
                    counter[num] -=1
                    backtrack(perm, counter)
                    perm.pop()
                    counter[num] +=1
            
        backtrack([], Counter(nums))
        return res
        
