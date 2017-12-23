class Solution(object):
    def firstUniqChar(self, s):
        letters = "abcdefghijklmnopqrstuvwxyz"
        indexes = [s.index(l) for l in letters if s.count(l) == 1]
        return min(indexes) if len(indexes) > 0 else -1
            
        
