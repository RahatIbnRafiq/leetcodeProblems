from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        if len(s) < len(p):return []
        map1 = Counter(p)
        start = 0
        end = start+len(p)
        c = Counter(s[start:end])
        result = []
        while end < len(s)+1:
            if c == map1:result.append(start)
            if c[s[start]] == 1:del c[s[start]]
            else: c[s[start]]-=1
            start+=1
            end+=1
            if end-1 < len(s):
                if s[end-1] in c: c[s[end-1]]+=1
                else:c[s[end-1]] = 1
        return result
            
            
        
                
            
            


s = Solution()
print s.findAnagrams("abab","ab")
        
