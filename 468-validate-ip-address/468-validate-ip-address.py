class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        ip4Arr = queryIP.split('.')
        ip6Arr = queryIP.split(':')
        
        if len(ip4Arr) == 4:
            for x in ip4Arr:
                if not (x.isdigit() and (x=='0' or x==x.lstrip('0')) and 0<=int(x)<=255):
                    return 'Neither'
            return 'IPv4'
        
        str = '1234567890abcdefABCDEF'
        if len(ip6Arr) == 8:
            for x in ip6Arr:
                if (len(x) == 0 or len(x) > 4):
                    return 'Neither'
                for ch in x:
                    if ch not in str:
                        return 'Neither'
            return 'IPv6'
        
        return 'Neither'
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
#         ip4Arr = queryIP.split('.')
#         ip6Arr = queryIP.split(':')
        
#         if len(ip4Arr) == 4:
#             for x in ip4Arr:
#                 if not (x.isdigit() and (x=='0'or x == x.lstrip('0')) and 0 <=int(x)<=255):
#                     return 'Neither'
#             return 'IPv4' 

#         str = '1234567890abcdefABCDEF'
#         if len(ip6Arr) == 8:
#             for x in ip6Arr:
#                 if len(x) < 1 or len(x) > 4:
#                     return 'Neither'
#                 for ch in x:
#                     if not ch in str:
#                         return 'Neither' 
#             return 'IPv6'
        
#         return 'Neither' 
                
        

        