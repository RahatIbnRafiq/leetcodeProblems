class Solution(object):
    def largestDivisibleSubset(self, nums):
        from copy import copy
        if not nums:return []
        n = len(nums)
        nums = sorted(nums)
        dp = [0] * n
        dp[0] = [nums[0]]
        
        for i in xrange(1,n):
            curr = nums[i]
            maxset = []
            for j in xrange(i):
                if curr%nums[j]==0:
                    temp = copy(dp[j])
                    if len(temp) > len(maxset):
                        maxset = temp
            maxset.append(nums[i])
            dp[i] = maxset
        
        
        res = []
        for temp in dp:
            if len(temp) > len(res):
                res = temp
        return res
                
        
