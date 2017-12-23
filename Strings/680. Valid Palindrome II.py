class Solution(object):
    def validPalindrome(self, s):
        count = 0
        p1,p2 = 0, len(s)-1
        
        while p1 < p2 and s[p1] == s[p2]:
            p1+=1
            p2-=1
        cand1 =(s[0:p1]+s[p1+1:])
        cand2 =(s[0:p2]+s[p2+1:])
        if cand1 == cand1[::-1]: return True
        if cand2 == cand2[::-1]: return True
        return False
