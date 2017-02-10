class Solution(object):
    def twoSum(self, numbers, target):
        dic = dict()
        for i in range(0,len(numbers)):
            if target-numbers[i] in dic:
                return [dic[target-numbers[i]]+1,i+1]
            else:
                dic[numbers[i]] = i
        return []
