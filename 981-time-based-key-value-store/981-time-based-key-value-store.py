class TimeMap:

    def __init__(self):
        self.store = defaultdict(defaultdict)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        while timestamp >= 1 and timestamp not in self.store[key]:
            timestamp -= 1
        return self.store[key][timestamp] if timestamp > 0 else ''
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)