class Solution:
    def maxDepth(self, s: str) -> int:
        max_count = 0
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                max_count = max(count, max_count)
                count -= 1
        return max_count


s = Solution()
print(s.maxDepth("(1+(2*3)+((8)/4))+1"))
print(s.maxDepth("(1)+((2))+(((3)))"))
print(s.maxDepth("1+(2*3)/(2-1)"))
print(s.maxDepth(""))
print(s.maxDepth("()(()())"))
print(s.maxDepth("()()"))
print(s.maxDepth("v"))
print(s.maxDepth("("))
