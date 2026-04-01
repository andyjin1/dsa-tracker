class Solution:
    def minWindow(self, s: str, t: str) -> str:
        valid = 0   
        window = defaultdict(int) 
        t_count = Counter(t)
        res_len = float('inf')

        l = 0
        for r, c in enumerate(s):
            window[c] += 1
            if c in t_count and window[c] == t_count[c]:
                valid += 1
            
            while valid == len(t_count):
                
                if r - l + 1 < res_len:
                    res_start = l 
                    res_len = r - l + 1 
                
                if s[l] in t_count and t_count[s[l]] == window[s[l]]:
                    valid -= 1 
                window[s[l]] -= 1
                l += 1 
        
        return "" if res_len == float('inf') else s[res_start:res_start+res_len]