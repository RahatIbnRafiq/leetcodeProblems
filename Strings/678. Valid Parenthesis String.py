class Solution(object):
    def checkValidString(self, s):
        from collections import deque
        opened, stars = deque(), deque()
        for i,c in enumerate(s):
            if c == '(':    opened.append(i)
            elif c == '*':  stars.append(i)
            else:
                if opened:  opened.pop()
                elif stars: stars.pop()
                else:       return False

        while opened and stars:
            while stars and stars[0] < opened[0]:
                stars.popleft()
            if stars:
                stars.popleft()
                opened.popleft()
        return not opened
