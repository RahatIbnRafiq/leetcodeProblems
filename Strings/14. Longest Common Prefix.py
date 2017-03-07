class Solution(object):
    def longestCommonPrefix(self, strs):
        res = []
        i = 0
        while True:
            try:
                tmp = strs[0][i]
                for str in strs[1:]:
                    if str[i] != tmp:return "".join(res)
                res.append(tmp)
                i+=1
            except Exception:return "".join(res)
        return "".join(res)
