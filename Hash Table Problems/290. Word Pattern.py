class Solution(object):
    def wordPattern(self, pattern, str):
        map1,map2 = {},{}
        strs = str.strip().split(" ")
        pattern = list(pattern)
        if len(pattern) != len(strs):return False
        for s,c in zip(strs,pattern):
            if s not in map1 and c not in map2:
                map1[s],map2[c] = c,s
            elif s in map1 and c in map2:
                if map1[s] != c or map2[c] != s:return False
            else:
                return False
        return True
        
