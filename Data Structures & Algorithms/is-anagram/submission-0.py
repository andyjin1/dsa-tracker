class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if len(s) != len(t):
            return False
        

        for i in range(len(s)):
            if sorted_s[i] != sorted_t[i]:
                return False 
    
        return True