class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # O(n) space 
        # O(n) time
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        
        return False