class Solution(object):
    def helper(self,path,nums):
        self.result[tuple(path)] = 1
        for i in range(0,len(nums)):
            self.helper(path+[nums[i]],nums[i+1:])
    def subsets(self, nums):
        nums.sort()
        self.result = dict()
        self.helper([],nums)
        return [list(x) for x in self.result.keys()]


s = Solution()
print s.subsets([1,2,3])
        
