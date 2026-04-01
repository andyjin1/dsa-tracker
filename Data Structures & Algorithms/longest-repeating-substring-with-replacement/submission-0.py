class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we want to expand the next letter as long as we are valid
        # we keep track of a replacement count, and that is the max number of different letter that we can have
        # we want to replace the non majority within the window
        # non majority is window size - max_freq, this number must not exceed k 

        count = defaultdict(int)
        max_freq = 0 # this tracks the frequency of majority, this never needs decrement because an update of res requires a new max freq. Any smaller max_freq would not have updated res
        # we only update res when we update max_freq to a higher value, therefore, we dont have to track the max_freq whenever the window max_freq changes 
        res = l = 0
        for r in range(len(s)):
            count[s[r]] += 1 
            max_freq = max(max_freq, count[s[r]]) # when we increment we might see a greater max freq
            while l <= r and (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res