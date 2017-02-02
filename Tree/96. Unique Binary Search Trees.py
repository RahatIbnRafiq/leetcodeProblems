class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0]*(n+1)
        f[0],f[1] = 1,1
        for i in range(2,n+1):
            for j in range(0,i):
                f[i] += f[j]*f[i-j-1]
        return f[-1]
        
        
