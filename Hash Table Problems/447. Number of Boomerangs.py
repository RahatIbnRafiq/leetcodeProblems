class Solution(object):
    def numberOfBoomerangs(self, points):
        res = 0
        for p in points:
            map = {}
            for q in points:
                a = p[0] - q[0]
                b = p[1] - q[1]
                map[a*a+b*b] = 1 + map.get(a*a+b*b,0)
            for k in map:
                res += map[k]*(map[k]-1)
        return res