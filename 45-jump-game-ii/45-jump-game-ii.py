class Solution:
    def jump(self, nums: List[int]) -> int:
        curEnd = 0
        maxEnd = 0
        res = 0
        
        for i in range(len(nums)-1):
            maxEnd = max(maxEnd, i+nums[i])
            if i == curEnd:
                curEnd = maxEnd
                res += 1
        return res 
