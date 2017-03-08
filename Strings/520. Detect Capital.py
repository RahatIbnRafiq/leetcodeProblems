class Solution(object):
    def detectCapitalUse(self, word):
        if not word: return True
        elif word[0] >='A' and word[0] <= 'Z':
            if word == word.upper():
                return True
            elif word[1:] == word[1:].lower():
                return True
        else:
            if word == word.lower():
                return True
        return False


s = Solution()
print s.detectCapitalUse("Leetcode")
