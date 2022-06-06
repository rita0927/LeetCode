class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())
        k = len(unique) - k
        
        def quickSelect(l,r):
            pivot_index = random.randint(l,r)
            pivot = count[unique[pivot_index]]
            unique[pivot_index], unique[r] = unique[r], unique[pivot_index]
            p = l
            
            for i in range(l,r):
                if count[unique[i]] < pivot:
                    unique[p], unique[i] = unique[i], unique[p]
                    p += 1
            unique[p], unique[r] = unique[r], unique[p]
            
            if k > p:
                return quickSelect(p+1, r)
            elif k < p:
                return quickSelect(l, p-1)
            else:
                return 
        quickSelect(0, len(unique) - 1)
        return unique[k:]
            
        
        
        

        

        
        
                
                
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      
        
        
        
     
                 
        
        
#         count = Counter(nums)
#         unique = list(count.keys())  
#         k = len(unique) - k
        
#         def quickSelect(l,r):

#             # pick the pivot randomly to avoid the worst-case of constantly bad chosen pivots
#             # pick an index between l and r (both included)
#             pivot_index = random.randint(l,r)
#             pivot = count[unique[pivot_index]]

#             # move pivot to end
#             unique[r], unique[pivot_index] = unique[pivot_index], unique[r]
#             # partition pointer 
#             p = l
            
#             for i in range(l,r):
#                 if count[unique[i]] < pivot:
#                     unique[i], unique[p] = unique[p], unique[i]
#                     p+=1
#             unique[r], unique[p] = unique[p], unique[r]
            
#             if k < p:
#                 quickSelect(l,p -1)
#             elif k > p:
#                 quickSelect(p + 1, r)
#             else:
#                 return 
            
#         quickSelect(0, len(unique) - 1)
#         return unique[k:]


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         count = Counter(nums)
#         unique = list(count.keys())
#         k = len(unique) - k
        
#         def quickSelect(l,r):

#             pivot = count[unique[r]] 
#             p = l
            
#             for i in range(l,r):
#                 if count[unique[i]] < pivot:
#                     unique[i], unique[p] = unique[p], unique[i]
#                     p +=1
#             unique[p], unique[r] = unique[r], unique[p]

#             if p == k:
#                 return
#             elif k <p:
#                 quickSelect(l, p - 1)
#             else:
#                 quickSelect(p + 1, r)
            
#         quickSelect(0, len(unique) - 1)
#         return unique[k:]
                    

                
        
        
        

        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         count = Counter(nums)  # {1:3, 2:2, 3:1}
#         unique = list(count.keys())  # [1,2,3]
#         k= len(unique) - k  # 1
        
# #         def partition(l,r):
            
# #             pivot = count[unique[r]]  
# #             p = l  
            
# #             for i in range(l,r):
                
# #                 if count[unique[i]] < pivot:
# #                     unique[i], unique[p] = unique[p], unique[i]
# #                     p+=1
# #             unique[p], unique[r] = pivot, unique[p]  
# #             return p  
            
        
#         def quickSelect(l,r):
#             if r == l:
#                 return 
#             # p = partition(l,r)
#             pivot = count[unique[r]]
#             p = l
            
#             for i in range(l,r):
                
#                 if count[unique[i]] < pivot:
#                     unique[i], unique[p] = unique[p], unique[i]
#                     p +=1
#             unique[p], unique[r] = unique[r], unique[p]
            
#             if k < p:
#                 quickSelect(l, p - 1)
#             elif k > p:
#                 quickSelect(p + 1, r)  
#             else:
#                 return 
            
#         quickSelect(0, len(unique) - 1)
#         return unique[k:]
            

            
        
   
        
       
        
        
        
#         count = Counter(nums) # {1:3, 2:2, 3:1}
#         unique = list(count.keys()) # [1,2,3]
#         k = len(unique) - k 
        
#         def partition(l, r):
#             pivot = count[unique[r]]
#             point = l
            
#             for i in range(l, r):
#                 if count[unique[i]] < pivot:
#                     unique[i], unique[point]= unique[point], unique[i]
#                     point +=1
#             unique[r], unique[point] = unique[point], unique[r]
            
#             return point 
            
#         def quickSelect(l,r):
#             # base case: the list contains only one element
#             if l == r:
#                 return 
            
#             p_index = partition(l,r)
            
#             if k == p_index:
#                 return 
            
#             elif k < p_index:
#                 quickSelect(l, p_index - 1)
#             else:
#                 quickSelect(p_index + 1, r)
                
#         quickSelect(0, len(unique) - 1)
        
#         return unique[k:]
                
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
             

        # bucket sort
        
#         count = Counter(nums)
#         freq = [[] for i in range(len(nums) + 1) ]

#         for n, c in count.items():
#             freq[c].append(n)
        
#         res = []
        
#         for i in range(len(freq)- 1, 0, -1):
            
#             for n in freq[i]:
#                 res.append(n)
                
#                 if len(res) == k:
#                     return res
        
# O(n), O(n)
# if all the elements are identical, then freq list has one element with value, the rest are empty. if all the elements are unique, then are the elements are in freq[1], then the time complexity is O(n) + O(n). Because the inner for loop won't be implemented on the empty list. It only loops through the freq[1], so the time complexity is 0(n): loop through the freq + O(n) :loop through freq[1]
        

    

    
    
        
        
#         count = Counter(nums)
        
#         # invoked with a comparison key function, count.get(key)
#         # print([count.get(key) for key in count.keys()])
        
#         return heapq.nlargest(k, count.keys(),count.get)
        
        
        
                
#         count = Counter(nums)
        
#         sortCount = sorted(count.items(), key = lambda x: x[1], reverse = True)

#         return [sortCount[i][0] for i in range(k)]
        
        
        
        
        
        
        
        
        