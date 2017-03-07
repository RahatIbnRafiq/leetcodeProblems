class Solution(object):
    def isValid(self, s):
        stack = []
        for i in range(0,len(s)):
            if s[i] in ['(','{','[']:
                stack.append(s[i])
            else:
                if len(stack)==0:return False
                tmp = stack.pop()
                if tmp == '(' and s[i] != ')':return False
                if tmp == '{' and s[i] != '}':return False
                if tmp == '[' and s[i] != ']':return False
        return len(stack)==0
