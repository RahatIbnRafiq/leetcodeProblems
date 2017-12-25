class Solution(object):
    def fourSumCount(self, A, B, C, D):
        c1 = {}
        for a in A:
            for b in B:
                c1[a+b] = c1.get(a+b,0)+1
        
        res = 0 
        
        for c in C:
            for d in D:
                res += c1.get((-1*(c+d)),0)
        return res
                    
