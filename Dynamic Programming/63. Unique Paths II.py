class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        row,col = len(grid),len(grid[0])
        dp = [[0 for i in range(col)]for j in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    dp[i][j] = '#'

        for i in range(row):
            for j in range(col):
                if dp[i][j] == '#':continue
                elif i == 0 and j==0:
                    if dp[i][j] == '#':return 0
                    dp[i][j] = 1
                elif i == 0:
                    if dp[i][j-1] == '#': dp[i][j] = '#'
                    else: dp[i][j] = 1
                elif j == 0:
                    if dp[i-1][j] == '#': dp[i][j] = '#'
                    else: dp[i][j] = 1
                else:
                    if dp[i-1][j] != '#':
                        dp[i][j] += dp[i-1][j]
                    if dp[i][j-1] != '#':
                        dp[i][j] += dp[i][j-1]
        return 0 if dp[-1][-1] == '#' else dp[-1][-1]
                    

s = Solution()
print s.uniquePathsWithObstacles([[1]])
        
