class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        # invoked with a comparison key function, count.get(key)
        # print([count.get(key) for key in count.keys()])
        
        return heapq.nlargest(k, count.keys(),count.get)
        
        
        
                
#         count = Counter(nums)
        
#         sortCount = sorted(count.items(), key = lambda x: x[1], reverse = True)

#         return [sortCount[i][0] for i in range(k)]
        
        
        
        
        
        
        
        
        