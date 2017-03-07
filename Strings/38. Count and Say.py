class Solution(object):
    def countAndSay(self, n):
        if n < 2: return str(n)
        res = "1"
        while n > 1:
            i = 0
            tmp = []
            while i < len(res):
                j = i+1
                count = 1
                while j < len(res) and res[i] == res[j]:
                    j+=1
                    count+=1
                tmp.append(str(count))
                tmp.append(str(res[i]))
                i = j
            res =  "".join(tmp)
            n-=1
        return res
