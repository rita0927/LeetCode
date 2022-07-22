class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix = self.get_prefix_sum(nums)
        
        res = float('-inf')
        sum2index = {0:0}
        for end in range(len(nums)):
            if prefix[end+1] - k in sum2index:
                length = end+1 - sum2index[prefix[end+1] -k]
                print(end+1)
                print(sum2index[prefix[end+1] -k])
                res = max(res, length)
            if prefix[end+1] not in sum2index:
                sum2index[prefix[end+1]] = end+1 
        return res if res != float('-inf') else 0
        
 
    def get_prefix_sum(self, nums):
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        return prefix
        
        
   

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         d = {}
#         prefix = 0
#         res = 0
        
#         for i in range(len(nums)):
#             prefix += nums[i]
            
#             # prefix includes all the previous num, the index + 1 (len of all the previous num) is the max for sure
#             if prefix == k:
#                 res = i + 1
            
#             # when the prefix - k in the dict, get rid of the complement to get the len of subarray 
#             if (prefix - k) in d:
#                 res = max(res, i - d[prefix - k])
#             # only save the first prefix to dict to get the max subarray 
#             if prefix not in d:
#                 d[prefix] = i
                
#         return res 
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         indices= {}
#         prefix = 0
#         res = 0
        
#         for i, n in enumerate(nums):
            
#             prefix +=n
            
#             if prefix == k:
#                 res = i + 1
            
#             if (prefix - k) in indices:
#                 res = max(res, i -indices[prefix-k])
            
#             if prefix not in indices:
#                 indices[prefix] = i
#         return res 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
        
        