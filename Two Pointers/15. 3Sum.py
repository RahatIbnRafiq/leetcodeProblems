class Solution(object):
    def threeSum(self, nums):
        def helper(nums, target, N, result, results):
            if len(nums)<N or N<2 or target < nums[0]*N or target > nums[-1]*N:
                return
            if N==2:
                left,right = 0,len(nums)-1
                while left < right:
                    s = nums[left]+nums[right]
                    if s == target:
                        results.append(result+[nums[left],nums[right]])
                        left+=1
                        while left < right and nums[left]==nums[left-1]:
                            left+=1
                    elif s < target:
                        left+=1
                    else:
                        right-=1
            else:
                for i in range(len(nums)):
                    if i == 0 or (i>0 and nums[i]!=nums[i-1]):
                        helper(nums[i+1:],target-nums[i],N-1,result+[nums[i]],results)
        results = []
        helper(sorted(nums),0,3,[],results)
        return results
