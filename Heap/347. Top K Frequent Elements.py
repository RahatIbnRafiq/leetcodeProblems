import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        d = dict()
        for n in nums:
            d[n] = d.get(n,0)+1
        heap = [(x[1],x[0]) for x in d.items()]
        heapq.heapify(heap)
        return [x[1] for x in heapq.nlargest(k,heap)]


s = Solution()
print s.topKFrequent([1,1,1,2,2,3],2)
