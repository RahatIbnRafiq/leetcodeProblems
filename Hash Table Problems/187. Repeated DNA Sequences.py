class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:return []
        start,end,map = 0,10,dict()
        result = set()
        while end <= len(s):
            map[s[start:end]] = map.get(s[start:end],0)+1
            if map[s[start:end]] > 1:result.add(map[s[start:end]])
            start+=1
            end+=1
        return [key for key in map.keys() if map[key]>1]
        
