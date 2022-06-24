class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = [[(0,0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        # if the last snap_id in the tuple matches current snaps_id
        if self.snaps[index][-1][0] == self.snap_id:
            # tuple is not mutable, need to replace the entire tuple
            self.snaps[index][-1] = (self.snap_id, val)
        # the snap_id doesn't match, need to append another update
        else:
            self.snaps[index].append((self.snap_id, val))
        
    def snap(self) -> int:
        self.snap_id +=1
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        lst = self.snaps[index]
        l = 0
        r = len(lst)-1
        
        while l <= r:
            mid = l + (r-l)//2
            if snap_id < lst[mid][0]:
                r = mid - 1
            elif snap_id >= lst[mid][0]:
                l = mid + 1

        if r == -1: return 0
        return lst[r][1] 

            
        
        
        

        
        

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)




# class SnapshotArray:

#     def __init__(self, length: int):
#         self.snaps = defaultdict(defaultdict)
#         self.snap_id = 0

#     def set(self, index: int, val: int) -> None:
#         self.snaps[self.snap_id][index] = val
        
#     def snap(self) -> int:
#         self.snap_id +=1
#         return self.snap_id - 1
        

#     def get(self, index: int, snap_id: int) -> int:
#         while snap_id >= 0:
#             if index in self.snaps[snap_id]:
#                 return self.snaps[snap_id][index]
#             snap_id -= 1
#         return 0
        