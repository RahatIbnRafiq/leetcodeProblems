from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        c = Counter(magazine)
        for char in ransomNote:
            try:
                if c[char] > 0: c[char]-=1
                else: return False
            except Exception:return False
        return True
