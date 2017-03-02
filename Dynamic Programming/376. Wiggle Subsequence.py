class Solution(object):
    def wiggleMaxLength(self, nums):
        if (len(nums) < 2):
            return len(nums)
        diffs = []
        for i in range(1, len(nums)):
            x = nums[i] - nums[i - 1]
            if (x != 0):
                diffs.append(x)
        if (not diffs):
            return 1
        cnt = 1 
        for i in range(1, len(diffs)):
            prod = diffs[i] * diffs[i - 1]
            if (prod < 0):
                cnt += 1
                
        return cnt + 1
