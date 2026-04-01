class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: 

        res = []
        q = collections.deque()
        l = 0
        for r, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            
            q.append(r)

            if q[0] < l:
                q.popleft()

        
            if r - l + 1 == k:
                res.append(nums[q[0]])
                l += 1 
            
        return res