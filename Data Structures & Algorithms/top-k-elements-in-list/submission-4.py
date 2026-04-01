class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        freq = Counter(nums) # value:freq

        for val, freq in freq.items():
            heapq.heappush(min_heap, (freq, val))
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [val for _, val in min_heap]
        





