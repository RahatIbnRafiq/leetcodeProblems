class Solution(object):
    def maxSubArray(self, nums):
        max_so_far = max_ending_here = nums[0]
        for i in range(1,len(nums)):
            max_ending_here = max(nums[i],max_ending_here+nums[i])
            max_so_far = max(max_so_far,max_ending_here)
        return max_so_far

s = Solution()
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
