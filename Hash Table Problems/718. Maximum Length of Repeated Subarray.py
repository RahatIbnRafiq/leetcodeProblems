class Solution(object):
    def findLength(self, A, B):
        m,n = len(A),len(B)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i+1][j+1] = 1+dp[i][j]
        return max(max(row) for row in dp)
        
