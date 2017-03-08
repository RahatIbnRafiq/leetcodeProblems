class Solution(object):
    def countSegments(self, s):
        tokens = s.strip().split(" ")
        tokens = [t for t in tokens if t!=" " and len(t) > 0]
        return len(tokens)
