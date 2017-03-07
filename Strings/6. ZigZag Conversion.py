class Solution(object):
    def convert(self, s, numRows):
        if len(s) == 0: return s
        if len(s) < numRows: return s
        if numRows == 1: return s
        res = []
        for i in range(0,numRows):
            res.append([])
        count,i = 0,0
        while count < len(s):
            if i == 0:
                while i < numRows and count < len(s):
                    res[i].append(s[count])
                    i+=1
                    count +=1
            i = i-1
            if i == numRows -1:
                i-=1
                while i > 0 and count < len(s):
                    res[i].append(s[count])
                    i-=1
                    count+=1
            
            
        res = ["".join(x) for x in res]
        return "".join(res)
