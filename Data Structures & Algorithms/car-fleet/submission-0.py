class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target - position / speed will give us 

        # make them into pairs 

        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        
        for p, s in pairs:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # if the time it arrives is larger than they will never collide
                stack.pop()
            
        return len(stack)
