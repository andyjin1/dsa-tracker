class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # we expand the window as long as we do not have matching
        # we remove from the window when we do have matching to see if we can get a smaller substring
        count_t = defaultdict(int)
        count_s = defaultdict(int)
        res_len = float('inf')
        res = "" 
        match = 0
        for c in t:
            count_t[c] += 1
        l, r = 0, 0
        while r < len(s):
            to_add = s[r]
            count_s[to_add] += 1
            if to_add in count_t and count_s[to_add] == count_t[to_add]:
                match += 1      

            while l <= r and match == len(count_t):
                # check if this is smallest substring that we have encountered
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res = s[l:r + 1]
                to_remove = s[l]
                l += 1 
                count_s[to_remove] -= 1 
                # this should be previously satisfied
                if to_remove in count_t and count_s[to_remove] < count_t[to_remove]:              
                    match -= 1 
            r += 1
        return res
        
        # s="ADOBECODEBANC" cc = [A:1, D:1]