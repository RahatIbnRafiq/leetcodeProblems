import collections
class Solution(object):
    def findMaximumXOR(self, nums):
        def Trie(): 
            return collections.defaultdict(Trie)
        
        root = Trie()
        best = 0
        
        for num in nums:
            candidate = 0
            cur = this = root
            for i in range(32)[::-1]:
                curBit = num >> i & 1
                this = this[curBit]
                if curBit ^ 1 in cur:
                    candidate += 1 << i
                    cur = cur[curBit ^ 1]
                else:
                    cur = cur[curBit]
            best = max(candidate, best)
        return best
