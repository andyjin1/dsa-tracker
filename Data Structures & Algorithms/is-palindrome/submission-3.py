class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = [char.lower() for char in s if char.isalnum()]

        l, r = 0, len(cleaned_str) - 1 

        while l <= r:
        
            if cleaned_str[l] != cleaned_str[r]:
                return False 
            
            l += 1 
            r -= 1
        
        return True