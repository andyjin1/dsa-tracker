class MinStack:

    def __init__(self):
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append((val, val))
        else:
            curr_min = min(val, self.min_stack[-1][0])
            self.min_stack.append((curr_min, val))

    def pop(self) -> None:
        return self.min_stack.pop() 

    def top(self) -> int:
        return self.min_stack[-1][1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]
