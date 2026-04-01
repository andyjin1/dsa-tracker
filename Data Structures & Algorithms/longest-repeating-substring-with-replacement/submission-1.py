class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # find the continuous substring that contains at most k
        majority = 0
        l = 0 
        res = 0
        freq = {}
        for r, c in enumerate(s):
            freq[c] = freq.get(c, 0) + 1 
            majority = max(majority, freq[c])

            while (r - l + 1) - majority > k:
                freq[s[l]] -= 1 
                l += 1 
        
            res = max(res, r - l + 1)
            r += 1
    
        return res

        