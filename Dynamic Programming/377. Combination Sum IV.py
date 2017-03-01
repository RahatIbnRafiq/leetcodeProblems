class Solution(object):
    def combinationSum4(self, nums, target):
        nums = sorted(nums)
        dp = [0]*(target+1)
        dp[0] = 1
        
        for i in range(target+1):
            for num in nums:
                if num > i:
                    break
                if num == i:
                    dp[i]+=1
                if num  < i:
                    dp[i] += dp[i-num]
        return dp[-1]
        
