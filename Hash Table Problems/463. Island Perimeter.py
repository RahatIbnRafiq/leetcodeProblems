class Solution(object):
    def islandPerimeter(self, grid):
        islands,neighbours = 0,0
        
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == 1: 
                    islands+=1
                    if i+1 < len(grid) and grid[i+1][j] == 1: neighbours+=1
                    if j+1 < len(grid[0]) and grid[i][j+1] == 1: neighbours+=1
        return islands*4-2*neighbours
