class Solution(object):
    def frequencySort(self, s):
        s = list(s)
        map = dict()
        for c in s:
            map[c] = map.get(c,0)+1
        result = []
        for w in sorted(map, key=map.get, reverse=True):
            l = [w]*(map[w])
            result = result + l
        return "".join(result)



s = Solution()
print s.frequencySort("tree")
            
            
