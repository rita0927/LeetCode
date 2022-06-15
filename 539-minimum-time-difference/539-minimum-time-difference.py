class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for t in timePoints:
            h,m = t.split(':')
            times.append(int(h) * 60 + int(m))
        
        times.sort()
        res = 1440 + times[0] - times[-1]
        
        for i in range(1,len(times)):
            res = min(res, times[i] - times[i-1])
        
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
        