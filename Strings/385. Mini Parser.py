# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        stack, start = [], -1
        for i, c in enumerate(s):
            if c == '[':
                stack.append(NestedInteger())
            elif c == ']':
                # for last ], it is possible that there is only one NestedInteger
                if len(stack) > 1:
                    t = stack.pop()
                    stack[-1].add(t)
            elif c.isdigit() or c == '-':
                if start == -1:
                    start = i
                if i == len(s) - 1 or not s[i + 1].isdigit():
                    if stack:
                        stack[-1].add(NestedInteger(int(s[start:i + 1])))
                    else:
                        stack.append(NestedInteger(int(s[start:i + 1])))
                    start = -1
        return stack.pop()
        
