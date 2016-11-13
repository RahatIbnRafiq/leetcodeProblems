class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) < 2: return len(nums)
        i = 0
        for n in nums:
            if i == 0 or n>nums[i-1]:
                nums[i] = n
                i+=1
        return i
        
