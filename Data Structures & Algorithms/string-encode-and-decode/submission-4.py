class Solution:

    def encode(self, strs: List[str]) -> str:
        
        msg = ""
        for word in strs:
            msg += str(len(word)) + '#' + word
        
        return msg
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):

            j = i
            while s[j].isdigit():
                j += 1
            
            length = int(s[i:j])
            # 5#Hello5#World
            # j = 
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length 
        
        return res