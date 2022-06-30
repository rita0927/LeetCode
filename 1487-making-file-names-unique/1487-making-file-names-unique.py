class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d = defaultdict(int)

        for name in names:
            
            modified = name 
            
            # if name in d:
            c = d[name]
            
            while d[modified]:  
                modified = f'{name}({c})'
                c += 1  
                
            d[name] = c
            d[modified] = 1
                     
        return d.keys() 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dic = {}
        
#         for name in names:
            
#             modified = name
#             if name in dic:
#                 k = dic[name]
                
#                 while modified in dic:
#                     k+=1
#                     modified = f'{name}({k})'
#                 dic[name] = k
#             dic[modified] = 0
#         return dic.keys()    
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dic = {}
        
#         for name in names:
            
#             modified = name
            
#             if name in dic:
#                 k = dic[name]
                
#                 while modified in dic:
#                     k +=1
#                     modified = f'{name}({k})'
                    
#                 dic[name] = k            
#             dic[modified] = 0
            
#         return dic.keys()
        