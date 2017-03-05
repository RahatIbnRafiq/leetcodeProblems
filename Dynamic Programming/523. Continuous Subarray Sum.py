class Solution(object):
    def checkSubarraySum(self, A, k):
        P = [0] #P[i] = sum(A[:i]), mod abs(k) if k != 0
        for x in A:
            v = P[-1] + x
            if k: v %= abs(k)
            P.append(v)
        
        seen = set()
        for i in xrange(len(P) - 3, -1, -1):
            seen.add(P[i+2])
            if P[i] in seen:
                return True
        return False
