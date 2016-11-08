class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        map = dict()
        for i in range(0,len(nums)):
            if nums[i] not in map: map[nums[i]] = i
            else:
                if i - map[nums[i]] <=k:return True
                map[nums[i]] = i
        return False
        
