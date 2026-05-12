class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j, 1))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            r, c, distance = q.popleft()

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = distance
                    q.append((nr, nc, grid[nr][nc] + 1))
