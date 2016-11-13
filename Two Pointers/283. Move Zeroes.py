class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        j=0
        for n in nums:
            if n !=0:
                nums[i] = n
                i+=1
            else:
                j+=1
        while j:
            nums[i]=0
            i+=1
            j-=1
