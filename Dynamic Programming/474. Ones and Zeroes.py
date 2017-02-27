class Solution(object):
    def findMaxForm(self, strs, m, n):
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        def count(s):
            return sum(1 for c in s if c == '0'), sum(1 for c in s if c == '1')

        for z,o in [count(s) for s in strs]:
            for x in xrange(m,-1,-1):
                for y in xrange(n,-1,-1):
                    if x >=z and y>=o:
                        dp[x][y] = max(dp[x-z][y-o]+1,dp[x][y])
        return dp[m][n]
            
            
        
