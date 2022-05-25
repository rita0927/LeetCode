class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        def sqToPosition(num):
            r = (num - 1) //n
            c = (num - 1) % n
            if r %2:
                c = n - 1 - c     
            return board[r][c]
        
        queue=deque([(1,0)])
        visited = set()
        
        while queue:
            
            num, move = queue.popleft()
            visited.add(num)
            
            for i in range(1, 7):
                next = num + i
                if sqToPosition(next) != -1:
                    next= sqToPosition(next)
                if next == n**2:
                    return move + 1
                if next not in visited:
                    queue.append((next, move + 1))
        return -1 
                
        
        
        