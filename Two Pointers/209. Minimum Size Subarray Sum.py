class Solution(object):
    def minSubArrayLen(self, k, nums):
        count, i, j, n, res = 0, 0, 0, len(nums), float('inf')
        for j in range(len(nums)):
            count += nums[j]
            while i <= j and count >= k:
                res, count, i = min(res, j - i + 1),\
                                count - nums[i],\
                                i + 1
        return res if res < float('inf') else 0
