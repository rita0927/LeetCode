class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        index = bisect_left(arr, x)
        l = index-1
        r = index
        while r-l-1 <k:
            if l == -1:
                r += 1
                continue 
            if r == len(arr):
                l -= 1
                continue
            
            if abs(arr[l] - x) <= abs(arr[r]-x):
                l-=1
            else:
                r += 1
            print(l, r)
        return arr[l+1:r]
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
  
#         l = -1
#         r = len(arr) - k 
        
#         while l + 1 != r:
#             mid = (l+r)//2
#             if x-arr[mid] <= arr[mid + k] - x:
#                 r= mid
#             else:
#                 l = mid   
                
#         return arr[r:r+k]
        
     
    
    
    
    
    
    
    
        
        
        
        

#         l = 0 
#         r = len(arr) - k
        
#         while l< r:
#             mid = (l+r)//2
#             if x-arr[mid] <= arr[mid+k] - x:
#                 r = mid
#             else:
#                 l = mid + 1
   
#         return arr[l:l+k]
        
        
        
        
        
        
        
        
        
     
        
        
        
        
#         if len(arr) == k:
#             return arr
        
#         l = -1
#         r = len(arr)
        
#         # find the index range of x
#         # x may not be in the range of arr[0], arr[-1]
#         while l + 1 != r:
#             mid = (l+r) //2
#             if x >= arr[mid]:
#                 l = mid
#             else:
#                 r = mid 
#         # if x < than arr[0], l = -1. if x > arr[-1], r = len(arr)
        
#         # start with r-l=1, 0 element from arr
#         while r-l-1 < k:
            
#             # reach the left boundary (or x < arr[0])
#             if l == -1:
#                 r += 1
#                 continue
            
#             # reach the right boundary ( or x > arr[-1])
#             if r == len(arr):
#                 l -= 1
#                 continue 
            
#             # based on the question, |a - x| <= |b - x| is considered closer 
#             if abs(arr[l] - x) <= abs(arr[r] - x):
#                 l -= 1
#             else:
#                 r += 1
#         # either l or r is included in the res 
#         return arr[l+1:r]
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # O(log(N) + k) where N is the len of arr. log(N) for binary search, k for expanding window
#         # 0(1)
#         if len(arr) == k:
#             return arr
        
#         l = -1
#         r = len(arr)
        
#         while l + 1 != r:
#             mid = (l+r)//2
#             if x >= arr[mid]:
#                 l = mid
#             else: 
#                 r = mid
   
#         while r-l-1 < k:
#             if l == -1:
#                 r +=1
#                 continue
#             if r == len(arr):
#                 l -= 1
#                 continue 
    
#             if abs(arr[l]-x) <= abs(arr[r]-x):
#                 l -= 1
#             else:
#                 r += 1
                
#         return arr[l+1:r]
                
            
        
