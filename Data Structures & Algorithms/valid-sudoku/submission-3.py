class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_seen=collections.defaultdict(set)
        row_seen=collections.defaultdict(set)
        square_seen=collections.defaultdict(set)   #key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue 
                if board[r][c] in row_seen[r] or \
                board[r][c] in col_seen[c] or \
                board[r][c] in square_seen[(r//3,c//3)]:  
                    #row_seen[r] is a hash set of all vals in that row r
                    return False 
                col_seen[c].add(board[r][c])
                row_seen[r].add(board[r][c])
                square_seen[(r//3,c//3)].add(board[r][c])
        return True 
                