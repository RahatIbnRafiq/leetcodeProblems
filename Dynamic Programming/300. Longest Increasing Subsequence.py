class Solution(object):
    def lengthOfLIS(self, nums):
        l = len(nums)
        dp = [1]*l
        for i in range(0,len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j]+1
        return max(dp) if len(dp) > 0 else 0
