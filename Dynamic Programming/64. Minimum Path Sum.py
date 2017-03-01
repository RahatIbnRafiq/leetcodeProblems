class Solution(object):
    def minPathSum(self, grid):
        if not grid:return 0
        row = len(grid)
        col = len(grid[0])
        dp = [[0 for x in range(col)]for y in range(row)]

        for i in range(row):
            for j in range(col):
                if i==0 and j==0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j]+dp[i][j-1]
                elif j == 0:
                    dp[i][j] = grid[i][j]+dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]

        return dp[-1][-1]



s = Solution()
print s.minPathSum([[1,2],[1,1]])
        
