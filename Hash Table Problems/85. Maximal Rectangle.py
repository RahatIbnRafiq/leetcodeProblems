class Solution(object):
    
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        s1 = []
        s2 = []
        m = heights[0]*1
        s1.append(0)
        s2.append(heights[0])
        for i in range(1,len(heights)):
            if heights[i] > s2[-1]:
                s1.append(i)
                s2.append(heights[i])
            elif heights[i] < s2[-1]:
                t = s1[-1]
                while s2 and s2[-1] > heights[i]:
                    area = s2[-1]*(i-s1[-1])
                    m = max(area,m)
                    s2.pop()
                    t = s1.pop()
                s2.append(heights[i])
                s1.append(t)
        h = len(heights)
        while s2:
            p = s1.pop()
            q = s2.pop()
            area = q*(h-p)
            m = max(m,area)
        return m
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        temp = [[0 for x in matrix[0]] for j in matrix]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                temp[i][j] = int(matrix[i][j])


        row1 = temp[0]
        max_area = self.largestRectangleArea(row1)

        for row2 in temp[1:]:
            for i in range(0,len(row1)):
                if  row2[i] == 0:
                    row1[i] = 0
                else:
                    row1[i] += row2[i]
            max_area = max(max_area,self.largestRectangleArea(row1))
        
        return max_area
