class Solution(object):
    def helper(self,path,nums,idx):
        if len(path) > 1:
            self.result.append(path)
        unique = []
        for i in range(idx,len(nums)):
            if idx > 0 and nums[i] < nums[idx-1]:continue
            if nums[i] in unique:continue
            unique = unique+[nums[i]]
            self.helper(path+[nums[i]],nums,i+1)
                
    def findSubsequences(self, nums):
        self.result = []
        self.helper([],nums,0)
        return self.result

s = Solution()
print s.findSubsequences([1,3,5,7])
        
        
