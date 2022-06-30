class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = 10 **9 + 7 
        horizontalCuts.extend([0,h])
        verticalCuts.extend([0,w])
        horizontalCuts.sort()
        verticalCuts.sort()
        
        
        def getMaxDiff(arr):
            diff = 0
            for i in range(len(arr)-1):
                diff = max(diff, arr[i+1] - arr[i])
            return diff
        
        return (getMaxDiff(horizontalCuts) * getMaxDiff(verticalCuts)) % mod

        
        