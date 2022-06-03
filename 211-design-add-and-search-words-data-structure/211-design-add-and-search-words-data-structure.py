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
        
        trie = self.dict
        
        def dfs(node, index):
            
            if index == len(word):
                return True if 'isWord' in node else False

            
            if word[index] not in node and word[index] !='.':
                return False
            elif word[index] == '.':
                for key in node:
                    if key != 'isWord' and dfs(node[key], index+1):
                        return True
            else:
                return dfs(node[word[index]], index + 1)
        
        return dfs(trie, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)