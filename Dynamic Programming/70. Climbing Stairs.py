class Solution(object):
    def climbStairs(self, n):
        if n < 3: return n
        steps = [0 for i in xrange(0,n+1)]
        steps[0] = 0
        steps[1] = 1
        steps[2] = 2
        for i in xrange(3,n+1):
            steps[i] = steps[i-1]+steps[i-2]
        return steps[-1]
        
