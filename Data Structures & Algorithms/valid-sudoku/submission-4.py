import collections 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # start with creating dictionaries of sets for each row, col and square
        row_seen = collections.defaultdict(set)
        col_seen=collections.defaultdict(set)
        square_seen=collections.defaultdict(set)

        for r in range(9):      # O(N^2)
            for c in range(9):
                if board[r][c] == ".":
                    continue 
                if board[r][c] in row_seen[r] or board[r][c] in col_seen[c] or board[r][c] in square_seen[(r//3),c//3]:
                    return False 
                col_seen[c].add(board[r][c])
                row_seen[r].add(board[r][c])
                square_seen[(r//3,c//3)].add(board[r][c])
        return True 


                