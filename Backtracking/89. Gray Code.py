class Solution(object):
    def grayCode(self, n):
        results = [0]
        for i in range(n):
            temp = [x + pow(2,i) for x in results]
            results = results+temp[::-1]
        return results

s = Solution()
print s.grayCode(3)
        
