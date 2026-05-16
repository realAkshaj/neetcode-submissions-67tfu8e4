class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        q = deque()

        for r in range(rows):

            if board[r][0] == "O":
                q.append((r,0))
            if board[r][cols-1] == 'O':
                q.append((r,cols-1))
        
        for c in range(cols):

            if board[0][c] == "O":
                q.append((0,c))
            if board[rows-1][c] == "O":
                q.append((rows-1,c))
        
        while q:

            r,c = q.popleft()
            board[r][c] = "T"
            for dr,dc in directions:

                nr,nc = dr + r, dc + c
                if (0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O"):
                    q.append((nr,nc))
                

        for r in range(rows):
            for c in range(cols):

                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):

                if board[r][c] == "T":
                    board[r][c] = "O"
        
        
