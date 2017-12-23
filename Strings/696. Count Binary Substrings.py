class Solution(object):      
    def countBinarySubstrings(self, s):
        pre = 0
        cur = 1
        res = 0
        for i in xrange(1,len(s)):
            if s[i] == s[i-1]:
                cur +=1
            else:
                pre = cur
                cur = 1
            if pre >= cur:
                res +=1
        return res
