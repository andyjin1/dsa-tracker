class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_nums = Counter(nums)
        pq = []
        for val, freq in count_nums.items():
            
            heapq.heappush(pq,(freq, val))
            if len(pq) > k:
                heapq.heappop(pq)
        
        return [val for _, val in pq]