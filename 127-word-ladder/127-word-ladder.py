class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        words = set(wordList)
        level = 0
        queue = deque([beginWord])
        
        while queue:
            size = len(queue)
            level += 1
            
            for i in range(size):
                word = queue.popleft()
                
                if word == endWord:
                    return level
                
                for j in range(len(word)):
                    for ch in string.ascii_lowercase:
                        new_word = word[:j] + ch + word[j+1:]
                        if new_word in words:
                            queue.append(new_word)
                            words.remove(new_word)
                  
        return 0
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         
#         # O(M^2 * N) where M is the length of each word and N is the number of words in the wordList. For each word (max length M) in the wordList, we iterate over its length to find all the intermediate words, N words and each has the length of M, tht total numnber of iteration is M*N. Forming the intermediate word takes O(M) for the string operation. The total is O(M^2 * N)
        
#         # O(M*N)
        
#         words = set(wordList)
        
#         if endWord not in words:
#             return 0
             
#         level = 0
#         queue = deque([beginWord])
        
#         while queue:
#             size = len(queue)
#             level += 1
                
#             for _ in range(size):
#                 word = queue.popleft()
#                 if word == endWord:
#                         return level 
                    
#                 for i in range(len(word)):

#                     for ch in string.ascii_lowercase:
#                         new_word = word[:i] + ch + word[i+1:]
#                         if new_word in words:
#                             words.remove(new_word)
#                             queue.append(new_word)
        
#         return 0
        

                
        
        
       
        
        
        
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
        