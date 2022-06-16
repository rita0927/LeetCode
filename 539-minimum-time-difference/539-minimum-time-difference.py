class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def convertToMinutes(t):
            h,m = t.split(':')
            return int(h) * 60 + int(m)
        
        times = [False] * 1440
        
        for t in timePoints:
            m = convertToMinutes(t)
            
            if times[m]:
                return 0
            
            times[m] = True
            
        res = float('inf')
        prev = 0
        min_m, max_m = float('inf'), float('-inf')
        
        for m in range(len(times)):
            
            if times[m]:
                # don't compare the pair until the min_m & prev are updated to the m
                if min_m != float('inf'):
                    res = min(res, m - prev)
                min_m = min(min_m, m)
                max_m = max(max_m, m)
                prev = m
        res = min(res, 1440+min_m - max_m)
        return res 
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
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
        