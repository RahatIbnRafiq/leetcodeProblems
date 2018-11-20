class Solution:
    def arrayPairSum(self, nums):
        mi, ma = 10000000, -10000000
        for i in range(0,len(nums)):
            if nums[i] > ma:
                ma = nums[i]
            if nums[i] < mi:
                mi =nums[i]

        bucket = dict()
        for n in nums:
            if n not in bucket:
                bucket[n] = 0
            bucket[n] += 1
        res = 0
        k = 0
        for i in range(mi,ma+1):
            if i in bucket:
                if k%2 == 0:
                    if bucket[i]%2 == 0:
                        p = int(bucket[i] / 2)
                    else:
                        p = int(bucket[i] / 2)+1
                    res += (i*p)
                else:
                    q = bucket[i] - 1
                    if q%2 == 0:
                        p = int(q / 2)
                    else:
                        p = int(q / 2)+1
                    res += (i * p)
                k += bucket[i]
        return res



s = Solution()
print(s.arrayPairSum([1,4,3,2]))