class Solution(object):
    def helper(self,left,right):
        while left >=0 and right < len(self.s) and self.s[left] == self.s[right]:
            self.res+=1
            left -=1
            right +=1
        
    def countSubstrings(self, s):
        self.s = s
        self.res = 0
        if not self.s:
            return 0
        for i in range(0,len(s)):
            self.helper(i,i)
            self.helper(i,i+1)
        return self.res
        