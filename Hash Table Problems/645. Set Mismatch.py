class Solution(object):
    def findErrorNums(self, nums):
        result = []
        m = -1
        d = dict()
        for n in nums:
            if n in d:
                result.append(n)
            else:
                d[n]=True
            if n > m:
                m = n
        for i in range(1,m+1):
            if i not in d:
                result.append(i)
                return result
        return result+[m+1]
            
