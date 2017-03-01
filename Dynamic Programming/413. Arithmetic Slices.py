class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        if not nums:return 0
        if len(nums) < 3: return 0
        dp = [0,0]
        count = 1
        for j in range(2,len(nums)):
            if nums[j] -nums[j-1] == nums[j-1]-nums[j-2]:
                dp.append(dp[j-1]+count)
                count+=1
            else:
                dp.append(dp[j-1])
                count = 1
        return dp[-1]
                
