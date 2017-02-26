class Solution(object):
    def longestPalindromeSubseq(self, s):
        if not s: return none
        if len(s) < 2:return 1
        if s == s[::-1]:
            return len(s)
        dp = [[0 for i in range(0,len(s))]for j in range(0,len(s))]
        for i in xrange(len(dp)-1,-1,-1):
            dp[i][i] = 1
            for j in xrange(i+1,len(dp)):
                if s[i] == s[j]:
                    dp[i][j] = 2+dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][-1]
