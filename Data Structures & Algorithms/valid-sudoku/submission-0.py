class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set) 
        col = defaultdict(set)
        box = defaultdict(set)

        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                
                if board[i][j] == '.':
                    continue
                
                if (board[i][j] in row[i] 
                or board[i][j] in col[j] or board[i][j] in box[(i // 3, j // 3)]):
                    return False 
            
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                box[(i//3 , j // 3)].add(board[i][j])
        
        return True