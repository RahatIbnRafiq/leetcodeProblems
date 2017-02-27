class Solution(object):
    def canPartition(self, nums):
        n = sum(nums)
        if n%2 == 1:return False
        n = n/2
        dp = [False for x in xrange(0,n+1)]
        dp[0]=True
        for num in nums:
            for j in xrange(n,0,-1):
                if j>= num:
                    dp[j] = dp[j] or dp[j-num]
        return dp[-1]

s = Solution()
print s.canPartition([1,5,9,5,2])
        
