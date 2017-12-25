class Solution(object):
    def leastBricks(self, wall):
        d = collections.defaultdict(int)
        for line in wall:
            i = 0
            for b in line[:-1]:
                i+=b
                d[i]+=1
        
        
        return len(wall)-max(d.values())
        
