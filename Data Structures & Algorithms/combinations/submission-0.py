class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        path = []
        res = []
        
        def backtrack(i):
            if i > n:
                if len(path) == k:
                    res.append(path.copy())
                return
                
            # take
            path.append(i)
            backtrack(i + 1)
            path.pop() 

            # dont take current
            backtrack(i + 1)
        
        backtrack(1)
        return res