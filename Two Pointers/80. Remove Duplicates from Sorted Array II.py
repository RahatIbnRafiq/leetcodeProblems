class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) < 3: return len(nums)
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-1] or n > nums[i-2]:
                nums[i] = n
                i+=1
        return i


s = Solution()
s.removeDuplicates([1,1,1,2,2,3])
        
