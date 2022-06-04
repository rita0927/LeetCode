class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(ch, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        m = len(board)
        n = len(board[0])
        dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        res = []
        
        def backtracking(row, col, parent):    
            
            ch = board[row][col]
            node = parent[ch]
            
            # check if we find a match of word
            # return default value False if the WORD_KEY doesn't exist
            word_match = node.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                res.append(word_match)

            
            # Before the EXPLORATION, mark the cell as visited 
            board[row][col] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for x,y in dir:
                nr, nc = row + x, col + y     
                if nr < 0 or nr >= m or nc < 0 or nc >= n or not board[nr][nc] in node:
                    continue

                backtracking(nr, nc, node)
        
            # End of EXPLORATION, we restore the cell
            board[row][col] = ch
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not node:
                parent.pop(ch)

        for row in range(m):
            for col in range(n):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return res    
























#         # ETL
# class Trie:
    
#     def __init__(self):
#         self.children = {}
#         self.isWord = False
    
#     def addWord(self, word):
        
#         trie = self
        
#         for ch in word:
#             if ch not in trie.children:
#                 trie.children[ch] = Trie()
#             trie = trie.children[ch]
        
#         trie.isWord= True



# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         m = len(board)
#         n = len(board[0])
#         res = set()
#         visited = set()
#         dir = [[-1,0], [1,0], [0,-1], [0,1]]
        
#         trie = Trie()
#         for word in words:
#             trie.addWord(word)
#             trie.isWord = False 
        
#         def backtrack(r,c, node, word):
#             if r < 0 or c < 0 or r >= m or c >= n or (r,c) in visited or board[r][c] not in node.children:
#                 return 

#             visited.add((r,c))
#             ch = board[r][c]
#             node = node.children[ch]
#             word.append(ch)
            
#             if node.isWord:
#                 res.add(''.join(word))
#                 node.isWord = False
            
#             for x,y in dir:
#                 nr = r + x
#                 nc = c + y
#                 backtrack(nr, nc, node, word)
                
#                 # must use remove, pop may pop up random element
#             visited.remove((r,c))
#             word.pop()
        
#         for r in range(m):
#             for c in range(n):
#                 backtrack(r,c, trie, [])
#         return res 
        
   

















        
        
        
        

        
        
# # ETL       
        
# class TrieNode(object):
#     def __init__(self):
#         self.word = None
#         self.children = {}


# class Trie(object):
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         root = self.root
#         for char in word:
#             root = root.children.setdefault(char, TrieNode())
#         root.word = word


# class Solution(object):
#     def search(self, i, j, root, board, m, n, r):
#         char = board[i][j]
#         if not (char and char in root.children):
#             return

#         board[i][j], root = None, root.children[char]

#         if root.word:
#             r.append(root.word)
#             root.word = None

#         for x, y in ((0, -1), (-1, 0), (0, 1), (1, 0)):
#             ii, jj = i + x, j + y
#             if 0 <= ii < m and 0 <= jj < n:
#                 self.search(ii, jj, root, board, m, n, r)

#         board[i][j] = char

#     def findWords(self, board, words):
#         if not board:
#             return []

#         tree = Trie()
#         [tree.insert(word) for word in words]

#         m, n, r = len(board), len(board[0]), []

#         for i, row in enumerate(board):
#             for j, char in enumerate(row):
#                 self.search(i, j, tree.root, board, m, n, r)
#         return r
        