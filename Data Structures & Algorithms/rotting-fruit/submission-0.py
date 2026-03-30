class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        time, fresh = 0,0

        rows,cols = len(grid),len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r,c])

        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        while queue and fresh > 0:

            for i in range(len(queue)):
                r,c = queue.popleft()

                for dr,dc in directions:
                    new_row = dr + r
                    new_col = dc + c

                    if (min(new_row,new_col) < 0 or 
                        new_col == cols or new_row == rows or 
                        grid[new_row][new_col] != 1):
                        continue
                    
                    grid[new_row][new_col] = 2
                    queue.append([new_row,new_col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
                    


