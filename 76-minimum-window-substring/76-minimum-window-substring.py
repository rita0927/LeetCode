class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        dictT = Counter(t)
        dictS = defaultdict(int)
        l = 0
        res = ''
        count = 0
        
        for r, ch in enumerate(s):
            if dictT[ch]:
                dictS[ch] += 1
                
                if dictT[ch] >= dictS[ch]:
                    count += 1
            if count == len(t):
                while dictS[s[l]] > dictT[s[l]] or s[l] not in dictT:
                    if dictS[s[l]] > dictT[s[l]]:
                        dictS[s[l]] -= 1
                    l += 1
                
                if not res or len(res) > r-l+1:
                    res = s[l:r+1]
        return res 
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dicS = defaultdict(int)
#         dicT = defaultdict(int)
#         count, start = 0, 0
#         result = ""
#         for char in t:
#             dicT[char] = dicT[char] + 1

#         for i, char in enumerate(s):
#             if dicT[char] > 0:
#                 dicS[char] = dicS[char] + 1
#                 if dicT[char] >= dicS[char]:
#                     count += 1
#             # dicS[char] = dicS[char] + 1
#             # if dicT[char] >= dicS[char]:
#             #     count += 1

#             if count == len(t):
#                 while dicT[s[start]] < dicS[s[start]] or not dicT[s[start]]:
#                     if dicT[s[start]] < dicS[s[start]]:
#                         dicS[s[start]] -= 1
#                     start += 1
#                 if not len(result) or i + 1 - start < len(result):
#                     result = s[start : i + 1]
#         return result

        