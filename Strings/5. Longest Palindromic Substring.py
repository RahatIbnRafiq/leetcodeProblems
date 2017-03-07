class Solution(object):
    def helper(self,s,l,r):
        while l > -1 and r<len(s) and s[l] == s[r]:
            r+=1
            l-=1
        return s[l+1:r]
    def longestPalindrome(self, s):
        res = s[0]
        for i in range(0,len(s)):
            tmp = self.helper(s,i,i)
            if len(tmp) > len(res): res = tmp

            tmp = self.helper(s,i,i+1)
            if len(tmp) > len(res): res = tmp
        return res
