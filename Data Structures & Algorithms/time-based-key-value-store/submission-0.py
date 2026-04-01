from bisect import bisect_left
class TimeMap:

    def __init__(self):
        self.key_value = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        history = self.key_value[key]
        idx = bisect_left(history, (timestamp + 1,)) - 1    
        
        return history[idx][1] if idx >= 0 else ""
