class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k=len(nums)-k
        
        def quickSelect(l,r):
            if l==r:
                return 
            pivot_index = random.randint(l,r)
            pivot=nums[pivot_index]
            nums[pivot_index], nums[r]=nums[r], nums[pivot_index]
            
            p=l
            for i in range(l,r):
                if nums[i]<pivot:
                    nums[i],nums[p]=nums[p],nums[i]
                    p+=1
            nums[p],nums[r]=nums[r],nums[p]
            
            if k<p:
                return quickSelect(l,p-1)
            elif k>p:
                return quickSelect(p+1,r)
            return 
        
        quickSelect(0,len(nums)-1)
        return nums[k]
                
            
        
        
        
        
        

        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # return heapq.nlargest(k, nums)[-1]
        
      
        
        
        
#         heap = []
        
#         for n in nums:
#             heapq.heappush(heap,n)
            
#             if len(heap) > k:
#                 heapq.heappop(heap)
#         return heap[0]
        

            
        
        
    
        
        
        
#         # O(n), O(1)
        
#         k = len(nums) -k
        
#         def quickSelect(l,r):
#             if l == r:
#                 return
#             pivot_index = random.randint(l,r)
#             pivot = nums[pivot_index]
#             nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
#             p = l
            
#             for i in range(l,r):
#                 if nums[i] < pivot:
#                     nums[i], nums[p] = nums[p], nums[i]
#                     p+=1
#             nums[p], nums[r] = nums[r], nums[p]
            
#             if k< p:
#                 quickSelect(l, p - 1)
#             elif k > p:
#                 quickSelect(p + 1, r)
#             else:
#                 return
#         quickSelect(0, len(nums) - 1)
#         return nums[k]
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         k = len(nums) - k 
        
#         def quickSelect(l,r):
#             pivot, p = nums[r], l
            
#             for i in range(l,r):
#                 if nums[i] < pivot:
#                     nums[i], nums[p] = nums[p], nums[i]
#                     p+=1
#             nums[p], nums[r] = pivot, nums[p]
            
#             if k <p:
#                 return quickSelect(l, p-1)
#             elif k >p:
#                 return quickSelect(p + 1, r)
#             else:
#                 return nums[p]
#         return quickSelect(0, len(nums) - 1)
        
        
        
        
      
        
        
        
        
        
        
        
#       def mergeSort(nums):
#         if len(nums)<2:
#           return nums
#         left = nums[:len(nums)//2]
#         right = nums[len(nums)//2:]

#         mergeSort(left)
#         mergeSort(right)

#         left_index = 0
#         right_index = 0
#         index = 0

#         while left_index <len(left) and right_index <len(right):
#           if left[left_index] >right[right_index]:
#             nums[index] = left[left_index]
#             left_index+=1
#           else:
#             nums[index] = right[right_index]
#             right_index+=1
#           index+=1

#         while left_index <len(left):
#           nums[index] = left[left_index]
#           left_index+=1
#           index+=1

#         while right_index <len(right):
#           nums[index] = right[right_index]
#           right_index +=1
#           index+=1
        
#       mergeSort(nums)  
#       return nums[k-1]

        