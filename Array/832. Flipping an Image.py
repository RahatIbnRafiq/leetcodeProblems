class Solution:
    def flipAndInvertImage(self, A):
        l1 = len(A)
        l2 = len(A[0])
        B = [[1 for i in range(l2)] for j in range(l1)]
        for i in range(0,l1):
            for j in range(0,l2):
                if(A[i][l2-j-1]):
                    B[i][j] = 0
        return B