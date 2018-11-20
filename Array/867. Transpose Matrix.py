class Solution:
    def transpose(self, A):
        r,l = len(A),len(A[0])
        res = [[0 for i in range(r)] for j in range(l)]
        for i in range(0,r):
            for j in range(0,l):
                res[j][i] = A[i][j]
        return res
