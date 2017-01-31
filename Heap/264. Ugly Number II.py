import sys
class Solution(object):
    def nthUglyNumber(self, n):
        factors = [2,3,5]
        indices = [0]*len(factors)
        uglies = [sys.maxsize]*n
        uglies[0] = 1
        for i in xrange(1,n):
            for j in xrange(0,len(factors)):
                uglies[i] = min(uglies[i],(factors[j]*uglies[indices[j]]))
            for j in xrange(0,len(factors)):
                indices[j] += (uglies[i] == factors[j]*uglies[indices[j]])
        return uglies[-1]

s = Solution()
print s.nthUglyNumber(10)
            
