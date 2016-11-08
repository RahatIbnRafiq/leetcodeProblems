from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        map1,map2 = Counter(s),Counter(t)
        for key in map2.keys():
            if key not in map1:return key
            if key in map1 and map1[key]!=map2[key]:return key
        return None
            
        
