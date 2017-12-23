class Solution(object):
    def checkRecord(self, s):
        if "LLL" in s or s.count("A") > 1:return False
        return True
        
