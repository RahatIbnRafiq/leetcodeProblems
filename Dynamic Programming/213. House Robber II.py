class Solution(object):
    def helper(self,nums):
        if not nums:return 0
        yes = [x for x in nums]
        no = [0 for x in nums]
        yes[0] = nums[0]
        no[0] = 0
        for i in xrange(1,len(nums)):
            yes[i] = max(no[i-1]+nums[i],nums[i])
            no[i] = max(yes[i-1],no[i-1])
        return max(yes[-1],no[-1])
    def rob(self, nums):
        if not nums:return 0
        if len(nums) == 0:return 0
        if len(nums) == 1:return nums[0]
        if len(nums) == 2: return max(nums)
        n  = len(nums)
        return max(self.helper(nums[0:n-1]),self.helper(nums[1:n]))
        
