from collections import Counter
class Solution(object):
    def longestPalindrome(self, s):
        map = Counter(s)
        maxLength=0
        oddpresent = False
        for key in map.keys():
            if map[key]%2 == 0: maxLength+=map[key]
            else:
                oddpresent = True
                maxLength+=((map[key]/2)*2)
        return maxLength+1 if oddpresent else maxLength
        
