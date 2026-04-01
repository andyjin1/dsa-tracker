class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we can sort the input array 
        # after sorting, we can fix a target an run two sumII on the rest
        res = []
        nums.sort()
        for i in range(len(nums)):
            #  nums[i] is the number that we need to find the sum of 
    
            l = i + 1 
            r = len(nums) - 1 

            if i > 0 and nums[i - 1] == nums[i]:
                continue

            while l < r:
                three_s = nums[i] + nums[l] + nums[r]

                if three_s > 0:
                    # we are too large 
                    r -= 1 
                
                elif three_s < 0:
                    l += 1 

                else:
                    # we have found a pair 
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1 
                    r -= 1 
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1 
                    
        return res

