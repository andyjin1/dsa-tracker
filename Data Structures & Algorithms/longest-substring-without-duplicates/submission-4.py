class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = set()
        l = 0
        res = float('-inf')
        # expand window as long as window doesnt have repeating character
        for r, to_add in enumerate(s):
            
            while to_add in window:
                window.remove(s[l])
                l += 1
                
            
            # valid window
            res = max(r - l + 1, res)
            window.add(to_add)
        
        return res if res > float('-inf') else 0