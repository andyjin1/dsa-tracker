class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = [[] for _ in range(len(nums) + 1)]

        num_freq = Counter(nums)

        for val, freq in num_freq.items():
            count[freq].append(val)
        
        res = []

        for i in range(len(nums) ,-1,-1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res
                
        
        