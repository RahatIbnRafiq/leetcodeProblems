class Solution(object):
    def helper(self,path,s,nums):
        if s == self.target:
            self.result[tuple(path)] = 1
        elif s > self.target:
            return
        else:
            for i in range(0,len(nums)):
                if s+nums[i] <= self.target:
                    self.helper(path+[nums[i]],s+nums[i],nums[i+1:])
    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.result = dict()
        self.target = target
        self.helper([],0,candidates)
        return [list(x) for x in self.result.keys()]

s = Solution()
print s.combinationSum2([10, 1, 2, 7, 6, 1, 5],8)
        
