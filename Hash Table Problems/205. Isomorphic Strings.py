class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):return False
        s,t = list(s),list(t)
        map1,map2 = {},{}
        for a,b in zip(s,t):
            if a in map1 and b in map2:
                if map1[a] != b or map2[b] != a:return False
            elif a not in map1 and b not in map2: map1[a],map2[b] = b,a
            else:return False
        return True
        
