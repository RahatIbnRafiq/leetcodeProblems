
"""
used trie. other method with prefix and set search was faster but i just wanted to use trie to solve this problem.
"""
class Node:
    def __init__(self,c):
        self.c = c
        self.kids = dict()

class Solution(object):
    def longestWord(self, words):
        words = sorted(words, key = len,reverse=False)
        d = dict()
        results = []
        maxLength = 0
        result = ""
        for word in words:
            if len(word) == 1 and word not in d:
                d[word] = Node(word)
                if len(word) > maxLength:
                    result = word
                    maxLength = len(word)
                elif len(word) == maxLength and result > word:
                    result = word
            elif len(word)==1:
                if len(word) > maxLength:
                    result = word
                    maxLength = len(word)
                elif len(word) == maxLength and result > word:
                    result = word
                continue
            else:
                i = 0
                char = word[i]
                dd = d.get(char)
                prev = None
                while i < len(word)-1 and dd is not None:
                    prev = dd
                    dd = dd.kids.get(word[i+1])
                    i+=1
                    char = word[i]
                if i == len(word)-1:
                    prev.kids[word[i]] = Node(word[i])
                    if len(word) > maxLength:
                        result = word
                        maxLength = len(word)
                    elif len(word) == maxLength and result > word:
                        result = word
        return result
                
                    
                        
                
            
                    
                


s = Solution()
print(s.longestWord(["ts","e","x","pbhj","opto","xhigy","erikz","pbh","opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi","x","o"]))
