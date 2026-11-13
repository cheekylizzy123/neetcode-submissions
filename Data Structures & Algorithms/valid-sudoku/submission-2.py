class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #now passes row and sub-grid check, but not columns
        for row in range(len(board)):
            row_seen={}
            for i in range(len(board[row])):  #checks for row
                if board[row][i]!=".":
                    if board[row][i] not in row_seen:
                        row_seen[board[row][i]]=True 
                    else:
                        return False 
                c_seen={}
                for c in range(len(board)):   #checks for column 
                    if board[c][i] != ".":
                        if board[c][i] not in c_seen:
                            c_seen[board[c][i]]=True
                        else:
                            return False 
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                sub_three ={}
                for r in range(box_row,box_row+3):
                    for c in range(box_col,box_col+3):
                        if board[r][c]!=".":
                            if board[r][c] not in sub_three:
                                sub_three[board[r][c]] = True 
                            else:
                                return False
            
        return True 
                