class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        res = 0
        l = 0
        
        for r in range(len(s)):
            count[s[r]]+=1
            
            # occurance of the most frequent letter + k results in the longest res 
            # when window width - occurance of most frequent letter > k, need to move left pointer
            while (r-l+1) - max(count.values()) > k:
                # decrease the l pointer occurance before moving the pointer
                count[s[l]] -=1
                l+=1
            res = max(res, r-l+1)
        return res 