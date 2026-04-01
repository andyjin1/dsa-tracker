class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hashmap to count the occurences 
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        freq = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for number in freq[i]:
                res.append(number)
                if len(res) == k:
                    return res 


        