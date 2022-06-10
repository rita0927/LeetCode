class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
         
        words = set(wordList)
        level = 0
        queue = deque([beginWord])
        
        while queue:
            size = len(queue)
            level += 1
                
            for _ in range(size):
                word = queue.popleft()
                if word == endWord:
                        return level 
                    
                for i in range(len(word)):

                    for ch in string.ascii_lowercase:
                        new_word = word[:i] + ch + word[i+1:]
                        if new_word in words:
                            words.remove(new_word)
                            queue.append(new_word)
        
        return 0
        

                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         words = set(wordList)
#         level = 0
#         queue = deque([beginWord])
        
#         if endWord not in words:
#             return 0
        
#         while queue:
#             level_size = len(queue)
            
#             for _ in range(level_size):
#                 word = queue.popleft()
                
#                 if word == endWord:
#                     return level + 1
#                 letters = list(word)
                
#                 for i in range(len(letters)):
#                     temp = letters[i]
                    
#                     for ch in string.ascii_lowercase:
#                         letters[i] = ch
#                         newWord = ''.join(letters)
                        
#                         if newWord in words:
#                             queue.append(newWord)
#                             words.remove(newWord)
#                     letters[i] = temp
#             level +=1
#         return 0
        
                        
                    
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dictOfWords = {i: 1 for i in wordList}
#         queue = deque([beginWord])
#         level = 0

#         while queue:
#             size = len(queue)

#             for _ in range(size):
#                 word = queue.popleft()
#                 if word == endWord:
#                     return level + 1
#                 letters = list(word)

#                 for i in range(len(letters)):
#                     temp = letters[i]
#                     for ch in ascii_lowercase:
#                         letters[i] = ch
#                         newWord = "".join(letters)
#                         if newWord in dictOfWords:
#                             queue.append(newWord)
#                             dictOfWords.pop(newWord)
#                     letters[i] = temp
#             level += 1
#         return 0
        