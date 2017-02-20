class Solution(object):
    def findTargetSumWays(self, nums, S):
        if not nums:return 0
        dic = {nums[0]:1,-nums[0]:1} if nums[0]!=0 else{0:2}
        for i in range(1,len(nums)):
            temp = {}
            for d in dic:
                temp[d+nums[i]] = temp.get(d+nums[i],0)+dic.get(d,0)
                temp[d-nums[i]] = temp.get(d-nums[i],0)+dic.get(d,0)
            dic = temp
        return dic.get(S,0)
