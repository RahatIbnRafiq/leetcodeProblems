class NumArray(object):

    def __init__(self, nums):
        if nums:
            self.sums = [0 for x in nums]
            self.sums[0] = nums[0]
            for i in range(1,len(nums)):
                self.sums[i] = self.sums[i-1]+nums[i]
        else:
            self.sums = []
        

    def sumRange(self, i, j):
        if (len(self.sums)) > 0:
            if (i==0):return self.sums[j]
            return self.sums[j]-self.sums[i-1]
        else:
            return None
