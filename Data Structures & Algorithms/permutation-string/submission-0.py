class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count_s1 = [0] * 26
        count_s2 = [0] * 26

        for c in s1:
            count_s1[ord(c) - ord('a')] += 1
        l, r = 0, len(s1)
        for c in range(r):
            # add the inital window into count
            count_s2[ord(s2[c]) - ord('a')] += 1
        if count_s2 == count_s1:
            return True 
        while r < len(s2):
            count_s2[ord(s2[r]) - ord('a')] += 1 
            while r - l + 1 > len(s1):
                count_s2[ord(s2[l]) - ord('a')] -= 1 
                l += 1
                
                if count_s1 == count_s2:
                    return True
            r += 1
        return False
                
            



            