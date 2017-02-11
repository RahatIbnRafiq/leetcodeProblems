class Solution(object):
    def helper(self,path,s,nums):
        if len(path) == self.k:
            if s == self.target:
                self.result.append(path)
        elif len(path) > self.k:
            return
        else:
            for i in range(0,len(nums)):
                if s+nums[i] <= self.target:
                    self.helper(path+[nums[i]],s+nums[i],nums[i+1:])
    def combinationSum3(self, k, n):
        nums = [i for i in range(1,10)]
        self.result = []
        self.target = n
        self.k = k
        self.helper([],0,nums)
        return self.result


s = Solution()
print s.combinationSum3(3,9)
        
