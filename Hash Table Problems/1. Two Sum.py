class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i in range(0,len(nums)):
            if nums[i] in map:
                return [map[nums[i]],i]
            else:
                map[target-nums[i]] = i
        return []
        
