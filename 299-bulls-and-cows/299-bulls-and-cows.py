class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bull = 0
        cow = 0
        d = defaultdict(int)
        
        for i in range(len(guess)):
            s = secret[i]
            g = guess[i]
            
            if s == g:
                bull += 1
            else:
                cow += int(d[s] < 0) + int(d[g] > 0)
                d[s] += 1
                d[g] -= 1
        return f'{bull}A{cow}B'
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         bulls = 0
#         cows = 0
#         d = defaultdict(int)
        
#         for i in range(len(secret)):
#             s = secret[i]
#             g = guess[i]
            
#             if s == g:
#                 bulls += 1
#             else:
#                 # int(True) == 1, int(False) == 0
#                 # if d[s] < 0, cows += 1; if d[g] > 0: cows += 1
                
#                 cows += int(d[s] < 0) + int(d[g] > 0)
                
#                 # if d[s] < 0:
#                 #     cows += 1
#                 # if d[g] > 0:
#                 #     cows += 1
#                 d[s] += 1
#                 d[g] -= 1
#         return f'{bulls}A{cows}B'
                
            
            