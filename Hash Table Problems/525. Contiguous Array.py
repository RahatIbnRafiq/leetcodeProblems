class Solution(object):
    def findMaxLength(self, nums):
        count = 0
        max_length=0
        d = {0: 0}
        maxLength = 0
        
        for i, num in enumerate(nums, 1):
            print i,num
            if num == 0:
                count -= 1
            else:
                count +=1
            if count in d:
                maxLength = max(maxLength,i-d[count])
            else:
                d[count] = i
        return maxLength
                
        
