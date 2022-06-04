class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        def backtracking(row, col, parent):    
            
            letter = board[row][col]
            currNode = parent[letter]
            
            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)
            
            # Before the EXPLORATION, mark the cell as visited 
            board[row][col] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            # End of EXPLORATION, we restore the cell
            board[row][col] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords    
























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
        