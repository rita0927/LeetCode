class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = defaultdict(defaultdict)
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.snaps[self.snap_id][index] = val
        
    def snap(self) -> int:
        self.snap_id +=1
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        while snap_id >= 0:
            if index in self.snaps[snap_id]:
                return self.snaps[snap_id][index]
            snap_id -= 1
        return 0
        
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)