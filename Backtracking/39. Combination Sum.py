class Solution(object):
    def helper(self,path,s,nums):
        if s == self.target:
            self.result[tuple(path)] = 1
        elif s > self.target:
            return
        else:
            for i in range(0,len(nums)):
                self.helper(path+[nums[i]],s+nums[i],nums[i:])
        
    def combinationSum(self, candidates, target):
        candidates.sort()
        self.result = dict()
        self.target = target
        self.helper([],0,candidates)
        return [list(x) for x in self.result.keys()]


s = Solution()
print s.combinationSum([2, 3, 6, 7],7)
