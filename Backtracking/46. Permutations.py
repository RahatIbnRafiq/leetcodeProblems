class Solution(object):

    def helper(self,path,nums):
        if len(nums)==0:
            self.result.append(path)
        else:
            for i in range(0,len(nums)):
                self.helper(path+[nums[i]],nums[:i]+nums[i+1:])
    def permute(self, nums):
        self.result = []
        self.l = len(nums)
        self.helper([],nums)
        return self.result

s = Solution()
s.permute([1,2,3])
        
        
