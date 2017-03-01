class Solution(object):
    def countBits(self, num):
        if num == 0:return [0]
        if num == 1:return [0,1]
        if num == 2:return [0,1,1]
        if num==3:return [0,1,1,2]
        dp = [0 for x in range(num+1)]
        dp[0],dp[1],dp[2],dp[3] = 0,1,1,2
        for i in range(4,num+1):
            dp[i] = dp[i/2]+dp[i%2]
        return dp
        
        
