class Solution:
    def maxDepth(self, s: str) -> int:
        max_count = 0
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                if count > max_count:
                    max_count = count
                count -= 1
            elif '0' <= char <= '9' and count > max_count:
                max_count = count
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
