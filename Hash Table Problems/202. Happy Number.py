class Solution(object):
    def isHappy(self, n):
        map = {}
        while True:
            if n == 1:return True
            if n in map:return False
            else:map[n] = True
            n = str(n)
            res = 0
            for c in n:
                res +=int(c)*int(c)
            n = res
        return False
        
