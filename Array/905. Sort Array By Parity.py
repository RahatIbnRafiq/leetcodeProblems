class Solution:
    def sortArrayByParity(self, A):
        p1, p2 = 0, len(A) - 1
        while p1 < p2:
            while p1 < p2 and A[p1] & 1 == 0:
                p1 += 1
            while p1 < p2 and A[p2] & 1 != 0:
                p2 -= 1
            A[p1], A[p2] = A[p2], A[p1]
            p1 += 1
            p2 -= 1
        return A
