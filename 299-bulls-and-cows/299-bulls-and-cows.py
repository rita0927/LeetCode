class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls = 0
        count = [0] * 10
        cows = 0
        
        for i in range(len(secret)):
            s = int(secret[i])
            g = int(guess[i])
            
            if s == g:
                bulls+=1
                continue
            if count[s] > 0:
                cows += 1
            if count[g] < 0:
                cows += 1
                
                
            count[s] -= 1
            count[g] += 1
        
        return f'{bulls}A{cows}B'


                
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
                
            
            