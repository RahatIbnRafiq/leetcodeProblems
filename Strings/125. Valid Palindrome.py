class Solution(object):

    def check(self,char):
        if char >= '0' and char <='9':return True
        if char >= 'a' and char <='z':return True
        return False
        
    def isPalindrome(self, s):
        s = s.lower()
        l,r  = 0,len(s)-1
        while l < r:
            while l < r and self.check(s[l]) == False:
                l+=1
            while l < r and self.check(s[r]) == False:
                r-=1
            if l < r and s[l] != s[r]: return False
            l+=1
            r-=1
        return True
