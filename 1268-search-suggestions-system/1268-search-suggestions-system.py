class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        res = []
        products.sort()
        pos = 0
        prefix = ''
        
        for ch in searchWord:
            prefix += ch
            pos = bisect_left(products, prefix, pos)
            res.append([p for p in products[pos:pos+3] if p.startswith(prefix)])
        
        return res 
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# # Time - O(nlogn + mlogn), O(nlogn) for sorting, m is the length of searchWord, O(logn) is for binary search of the products for a prefix
# # Space - O(1)
        
#         products.sort()
#         res = []
#         pos = 0
#         prefix = ''
        
#         for ch in searchWord:
#             prefix += ch 
#             pos = bisect_left(products, prefix, pos)
#             res.append([p for p in products[pos: pos+3] if p.startswith(prefix)])
        
#         return res 
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# Time - O(nlogn + n*m), O(nlogn) for sorting 
# Space - O(N)         
        
        
#         res = []
#         # sort product in lexicographical order 
#         products.sort()
        
#         for i, ch in enumerate(searchWord):
#             temp = []
#             for p in products:
#                 if i < len(p) and p[i] == ch:
#                     temp.append(p)
                    
#             # update products to the words match searchWord[:i+1]
#             products = temp
#             # return up to 3 products for each prefix  
#             res.append(temp[:3])
        
#         return res 
        
        
        
        
        