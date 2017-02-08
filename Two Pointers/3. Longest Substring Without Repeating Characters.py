class Solution(object):
    def lengthOfLongestSubstring(self, s):
        usedchar = {}
        start = 0
        maxLength  = 0
        for i in range(0,len(s)):
            if s[i] in usedchar and start <= usedchar[s[i]]:
                start = usedchar[s[i]]+1
            else:
                maxLength = max(maxLength,i-start+1)
            usedchar[s[i]]  = i
        return maxLength
            
