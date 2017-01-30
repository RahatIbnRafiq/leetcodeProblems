import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        return heapq.nlargest(k,nums)
        
