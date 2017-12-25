class Solution(object):
    def findLHS(self, nums):
        from collections import Counter
        c = Counter(nums)
        maxLength = 0
        for key in c.keys():
            if key+1 in c:
                maxLength = max(maxLength,c[key]+ c[key+1])
        return maxLength
        
