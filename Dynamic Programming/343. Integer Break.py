class Solution(object):
    def integerBreak(self, n):
        dp = [0,0,1,2,4,6,9,12]
        if n < 8:return dp[n]
        for i in range(8,n+1):
            dp.append(max(3*dp[i-3],2*dp[i-2]))
        return dp[-1]
        
