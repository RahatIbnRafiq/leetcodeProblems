import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        heap = []
        for n1 in nums1:
            for n2 in nums2:
                if len(heap) < k:
                    heapq.heappush(heap,(-n1-n2,n1,n2))
                else:
                    if heap and -heap[0][0] > n1+n2:
                        heapq.heappop(heap)
                        heapq.heappush(heap,(-n1-n2,n1,n2))
                    else:break
        return [[x[1],x[2]] for x in heap]
                        

s = Solution()
print s.kSmallestPairs([1,2],[3],3)
                
                
        
