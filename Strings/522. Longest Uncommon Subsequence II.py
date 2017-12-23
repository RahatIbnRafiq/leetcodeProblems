class Solution(object):
    def findLUSlength(self, A):
        def subseq(w1, w2):
            #True iff word1 is a subsequence of word2.
            i = 0
            for c in w2:
                if i < len(w1) and w1[i] == c:
                    i += 1
            return i == len(w1)

        A.sort(key = len, reverse = True)
        for i, word1 in enumerate(A):
            if all(not subseq(word1, word2) 
                    for j, word2 in enumerate(A) if i != j):
                return len(word1)
        return -1
        
