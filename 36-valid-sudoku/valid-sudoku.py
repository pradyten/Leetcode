class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = 9
        for i in range(9):
            count = defaultdict(int)
            for j in range(9):
                if board[i][j] in count and board[i][j] != '.':
                    return False
                count[board[i][j]] = 1

        for i in range(9):
            count = defaultdict(int)
            for j in range(9):
                if board[j][i] in count and board[j][i] != '.':
                    return False
                count[board[j][i]] = 1

        for square in range(9):
            count = defaultdict(int)
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] in count and board[row][col] != '.':
                        return False
                    count[board[row][col]] = 1

        return True
        