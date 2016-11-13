class Solution(object):
    def threeSumClosest(self, nums, target):
        def helper(nums, N, result,target):
            if N==2:
                left,right = 0,len(nums)-1
                while left < right:
                    s = nums[left]+nums[right]
                    if abs(s-target) < abs(self.target-self.closest):
                        self.closest = s+sum(result)
                    if s > target:
                        right-=1
                    else:
                        left+=1
                        
            else:
                for i in range(len(nums)):
                    helper(nums[i+1:],N-1,result+[nums[i]],target-nums[i])
                        
        nums.sort()
        self.target = target
        self.closest = nums[0]+nums[1]+nums[2]
        helper(nums,3,[],target)
        return self.closest


s = Solution()
print s.threeSumClosest([1,2,4,8,16,32,64,128],82)
        
