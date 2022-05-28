class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        l = 0
        
        while l < len(chars):
            chars[index] = chars[l]
            index +=1
            
            r = l
            while r < len(chars) and chars[r] == chars[l]:
                r+=1
    
            if r-l >1:
                count = str(r-l)
                for n in count:     
                    chars[index] = n
                    index +=1
                
            l = r
              
        return index
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         index = 0
#         l = 0
        
#         while l < len(chars):
#             r = l
#             while r < len(chars) and chars[r] == chars[l]:
#                 r+=1

#             chars[index] = chars[l]
#             index +=1
            
#             if r-l >1:
#                 count = str(r-l)
#                 for n in count:                    
#                     chars[index] = n
#                     index +=1

#             l = r
              
#         return index
        
        
        
        
        
        
        
        
        
        
#         if len(chars) == 1: return 1
        
#         l =0 
        
#         for r in range(len(chars)):
#             if r == len(chars) - 1 and chars[r] == chars[l]:
#                 l+=1
#                 chars[l] = r-l
#                 break

            
#             if chars[l] != chars[r] and r-l > 1:
#                 l+=1
#                 chars[l] = r-l+1
#                 l+=1
#                 chars[l] = chars[r]
            
#         for _ in range(len(chars) -1 - l):
#             chars.pop()
                                                         
#         return l+1
                                                         
        
        
        
                    
                    
        