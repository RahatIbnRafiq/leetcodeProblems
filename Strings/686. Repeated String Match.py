import math
class Solution(object):
    def repeatedStringMatch(self, A, B):
        q = (len(B) - 1) // len(A) + 1
        if B in A*(q):return q
        elif B in A*(q+1):return q+1
        return -1
            
        
