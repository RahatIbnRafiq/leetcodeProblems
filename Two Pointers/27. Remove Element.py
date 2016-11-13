class Solution(object):
    def removeElement(self, nums, val):
        if len(nums)==0:return 0
        i = 0
        for n in nums:
            if n != val:
                nums[i] = n
                i+=1
        return i

s = Solution()
s.removeElement([1,2,4,4],3)
        
