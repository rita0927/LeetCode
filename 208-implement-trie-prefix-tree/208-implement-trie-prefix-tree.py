class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        
        trie = self.root
        
        for ch in word:
            if ch not in trie.children:
                trie.children[ch] = TrieNode()
            trie = trie.children[ch]      
        trie.isWord = True
         

    def search(self, word: str) -> bool:
        trie = self.root
        for ch in word:
            if ch not in trie.children:
                return False
            trie = trie.children[ch]
        
        return trie.isWord
        

    def startsWith(self, prefix: str) -> bool:

        trie = self.root
        
        for ch in prefix:
            if ch not in trie.children:
                return False 
            trie = trie.children[ch]
        return True
            
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)











# class Trie:

#     def __init__(self):
#       self.trie = {}


#     def insert(self, word: str) -> None:
#       t = self.trie
#       for ch in word:
#         if ch not in t:
#           t[ch] = {}
#         t = t[ch]
#       t['isWord'] = True


#     def search(self, word: str) -> bool:
#       t = self.trie
#       for ch in word:
#         if ch in t:
#           t=t[ch]
#         else:
#           return False
#       return 'isWord' in t

#     def startsWith(self, prefix: str) -> bool:
#       t = self.trie
#       for ch in prefix:
#         if ch in t:
#           t = t[ch]
#         else:
#           return False
#       return True