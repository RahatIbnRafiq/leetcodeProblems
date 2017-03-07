class Solution(object):
    def reverseVowels(self, s):
        if s is None: return s
        if len(s) < 2:return s
        s = list(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        l,r = 0,len(s)-1
        while l < len(s) and r > -1 and l < r:
            while l < len(s) and l < r and s[l] not in vowels:l+=1
            while r >-1 and l < r and s[r] not in vowels:r-=1
            if l > r:break
            else:
                s[l],s[r] = s[r],s[l]
                l+=1
                r-=1
        return "".join(s)
