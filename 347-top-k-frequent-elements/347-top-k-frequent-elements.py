class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        sortCount = sorted(count.items(), key = lambda x:x[1], reverse=True)
        
        return [sortCount[i][0] for i in range(k)]
        