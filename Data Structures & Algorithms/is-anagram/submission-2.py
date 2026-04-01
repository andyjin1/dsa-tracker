class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        
        count_t = defaultdict(int)
        count_s = defaultdict(int)

        for i in range(len(s)):
            char_t, char_s = t[i], s[i]

            count_t[char_t] += 1
            count_s[char_s] += 1 
        

        return count_t == count_s