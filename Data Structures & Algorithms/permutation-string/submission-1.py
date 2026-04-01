class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False 
        
        # fixed size sliding window
        # find if there is a substring that contains the same number of d
        l = 0
        match = 0
        s1_count = Counter(s1)  
        window_count = {}
        for r, c in enumerate(s2):
            window_count[c] = window_count.get(c, 0) + 1
        
            if c in window_count and s1_count[c] == window_count[c]:
                 match += 1
            
            if match == len(s1_count):
                return True 
            
            if r - l + 1 == len(s1):
                if s2[l] in s1_count and window_count[s2[l]] == s1_count[s2[l]]:
                    match -= 1
                window_count[s2[l]] -= 1 
                l += 1
            
            
        return False
            
            