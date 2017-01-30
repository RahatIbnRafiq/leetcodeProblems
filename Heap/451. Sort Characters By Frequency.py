import heapq
class Solution(object):
    def frequencySort(self, s):
        s = list(s)
        d = dict()
        for char in s:
            d[char] = d.get(char,0)+1
        heap = [(x[1],x[0]) for x in d.items()]
        heapq.heapify(heap)
        heap = heapq.nlargest(len(heap),heap)
        return ''.join(x[1]*x[0] for x in heap)



s = Solution()
print s.frequencySort("tree")
