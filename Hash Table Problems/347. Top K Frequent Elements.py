import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        h = []
        map = dict()
        for n in nums:
            map[n] = map.get(n,0)+1
        for key in map.keys():
            heapq.heappush(h,(map[key],key))
        return [x[1] for x in heapq.nlargest(k,h)]
            
        
