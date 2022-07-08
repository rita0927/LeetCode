class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # if x < arr[0]:
        #     return arr[:k]
        # if x > arr[-1]:
        #     return arr[-k:]
        
        if len(arr) == k:
            return arr
        
        l = -1
        r = len(arr)
        
        while l + 1 != r:
            mid = (l+r)//2
            if x >= arr[mid]:
                l = mid
            else: 
                r = mid
   
        while r-l-1 < k:
            if l == -1:
                r +=1
                continue
            if r == len(arr):
                l -= 1
                continue 
    
            if abs(arr[l]-x) <= abs(arr[r]-x):
                l -= 1
            else:
                r += 1
                
        return arr[l+1:r]
                
            
        
