import re
class Solution(object):
    def reverse(self,s,l,r):
        while l<r:
            s[l],s[r] = s[r],s[l]
            l+=1
            r-=1
            
    def reverseWords(self, s):
        s = s.strip()
        if len(s) < 2: return s
        s = re.sub(' +',' ',s)
        s = list(s)
        i = 0
        for j in range(0,len(s)):
            if s[j] == " ":
                self.reverse(s,i,j-1)
                i = j+1
        self.reverse(s,i,j)
        self.reverse(s,0,len(s)-1)
        return "".join(s).strip()
