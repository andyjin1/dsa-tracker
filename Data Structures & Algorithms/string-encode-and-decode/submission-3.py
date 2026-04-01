class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        for word in strs:
            msg += word + "😀"
        
        return msg
    def decode(self, s: str) -> List[str]:
        return s.split('😀')[0:-1]