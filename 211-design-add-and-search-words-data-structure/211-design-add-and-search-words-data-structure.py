class WordDictionary:

    def __init__(self):
        self.dict = {}
        
        

    def addWord(self, word: str) -> None:
        
        trie = self.dict
        
        for ch in word:
            if ch not in trie:
                trie[ch] = {}
                
            trie = trie[ch]
        
        trie['isWord'] = True
        

    def search(self, word: str) -> bool:
        
        def dfs(trie, index):
            if index == len(word):
                return True if 'isWord' in trie else False
            
            ch = word[index]
            
            if ch in trie:
                return dfs(trie[ch], index + 1)
            elif ch == '.':
                for key in trie:
                    if key != 'isWord' and dfs(trie[key], index + 1):
                        return True
            else:
                return False
            
        return dfs(self.dict, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)





# class WordDictionary:

#     def __init__(self):
#         self.dict = {}
        

#     def addWord(self, word: str) -> None:
#         trie = self.dict
        
#         for ch in word:
#             if ch not in trie:
#                 trie[ch] = {}
#             trie = trie[ch]
        
#         trie['isWord'] = True
        

#     def search(self, word: str) -> bool:
        
#         trie = self.dict
        
#         def dfs(node, index):
            
#             if index == len(word):
#                 return True if 'isWord' in node else False
            
#             ch = word[index]
            
#             if ch in node:
#                 return dfs(node[ch], index + 1)
#             elif ch == '.':
#                 for key in node:
#                     if key != 'isWord' and dfs(node[key], index + 1):
#                         return True
#             else:
#                 return False 

            
#         return dfs(trie, 0)