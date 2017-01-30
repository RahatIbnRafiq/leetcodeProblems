import heapq
import sys
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        uglies = [sys.maxsize]*n
        uglies[0]  = 1
        indices = [0]*len(primes)
        for i in xrange(1,n):
            for j in range(0,len(primes)):
                uglies[i] = min(uglies[i],primes[j]*uglies[indices[j]])
            for j in range(0,len(primes)):
                indices[j] += (uglies[i] == uglies[indices[j]]*primes[j])
        print uglies
            
                
            
            
            

s = Solution()
print s.nthSuperUglyNumber(12,[2, 7, 13, 19])
