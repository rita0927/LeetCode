class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        
        
        max_product = nums[0]
        min_product = nums[0]
        res = max_product
        
        for n in nums[1:]:
            temp = max_product
            max_product = max(max_product * n, min_product * n, n)
            min_product = min(min_product * n, temp * n, n)
            res = max(res, max_product)
        
        return res 

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         max_product = nums[0]
#         min_product = nums[0]
#         res = max_product
        
#         for n in nums[1:]:
#             # max_product will be updated later (times n)
#             temp = max_product
            
#             # add n to abandon previous product: example [-3,5], [0, 4]
#             max_product = max(max_product*n, min_product*n, n)
#             # example: 3* (-5), (-5) * 3, -5
#             min_product = min(temp*n, min_product*n, n)
#             res = max(res, max_product)
            
#         return res 
            


                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         maxProduct = nums[0]
#         minProduct = nums[0]
#         res = nums[0]

#         for i in range(1, len(nums)):
#             # save temp before maxProduct gets updated
#             cur = nums[i]
#             temp = maxProduct
#             maxProduct = max(max(maxProduct * cur, minProduct * cur), cur)
#             minProduct = min(min(minProduct * cur, temp * cur), cur)
#             res = max(maxProduct, res)
#         return res
        