class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def convert(t):
            h,m = t.split(':')
            return int(h)*60 + int(m)
        
        buckets = [False] * 1440
        
        for t in timePoints:
            m = convert(t)
            if buckets[m]:
                return 0
            buckets[m] = True             
            
        res = float('inf')
        high = float('-inf')
        low = float('inf')
        prev = 0      
        for m in range(1440):
            if buckets[m]:
                if low != float('inf'):
                    res = min(res, m - prev)     
                low = min(low, m)
                high = max(high, m)
                prev = m 
        return min(res, 1440+low-high)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # Bucket sort, time complexity O(n)

#         def convertToMinutes(t):
#             h,m = t.split(':')
#             return int(h) * 60 + int(m)
        
#         # create bucket for each min
#         times = [False] * 1440
        
#         for t in timePoints:
#             m = convertToMinutes(t)
#             # if two time points are the same (the times[m] was updated to True already)
#             if times[m]:
#                 return 0
            
#             times[m] = True
            
#         res = float('inf')
#         # track the prev time in the times (sorted buckets)
#         prev = 0
#         min_m, max_m = float('inf'), float('-inf')
        
#         # index of the times is the minute we want to sort
#         for m in range(len(times)):
#             # minutes in the timePoints are marked as True
#             if times[m]:
#                 # don't compare the pair until the min_m & prev are updated to the actual m
#                 if min_m != float('inf'):
#                     res = min(res, m - prev)
#                 min_m = min(min_m, m)
#                 max_m = max(max_m, m)
#                 prev = m
#         res = min(res, 1440+min_m - max_m)
#         return res 
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
#         # Olog(N), O(N) due to sort
#         times = []
#         for t in timePoints:
#             h,m = t.split(':')
#             times.append(int(h) * 60 + int(m))
        
#         times.sort()
#         # comparing the diff between last and first elements
#         # for loop compares the rest of the elements
#         res = (1440 + times[0]) - times[-1]
#         for i in range(1, len(times)):
#             res = min(res, times[i] - times[i-1])
        
#         return res 
        