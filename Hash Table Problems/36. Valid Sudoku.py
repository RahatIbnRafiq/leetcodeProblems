class Solution(object):
    def isValidSudoku(self, board):
        if not board:return False
        row = len(board)
        column = len(board[0])
        rowMap,columnMap,cellMap = set(),set(),set()
        for i in range(0,row):
            for j in range(0,column):
                if board[i][j]!='.':
                    val = board[i][j]
                    if (val,i) in rowMap: return False
                    if (val,j) in columnMap:return False
                    if (val,i/3,j/3) in cellMap:return False
                    rowMap.add((val,i))
                    columnMap.add((val,j))
                    cellMap.add((val,i/3,j/3))
        return True
                    
        
