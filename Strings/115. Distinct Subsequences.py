class Solution(object):
    def numDistinct(self, s, t):
        mem = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
        for row in range(0,len(mem)):
            for col in range(0,len(mem[0])):
                if row == col and row == 0:
                    mem[row][col] = 1
                elif row == 0:
                    mem[row][col] = 1
        s = list(s)
        t = list(t)

        for row in range(0,len(t)):
            for col in range(0,len(s)):
                if t[row] == s[col]:
                    mem[row+1][col+1] = mem[row][col]+mem[row+1][col]
                else:
                    mem[row+1][col+1] = mem[row+1][col]


        return mem[-1][-1]
