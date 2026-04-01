class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        num_set = set(nums)

        for num in nums:
            if num - 1 not in num_set:
                length = 1 
            
                while length + num in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest
                
            