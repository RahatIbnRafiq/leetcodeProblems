class Solution(object):
    def judgeCircle(self, moves):
        import collections
        c = collections.Counter(moves)
        return c['L'] == c['R'] and c['U'] == c['D']
