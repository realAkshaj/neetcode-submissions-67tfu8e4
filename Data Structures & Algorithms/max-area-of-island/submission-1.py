class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid),len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        max_area = 0
        

        def bfs(r,c):

            q = deque()
            q.append((r,c))
            grid[r][c] = 0
            area = 1

            while q:

                r,c = q.popleft()
                
                for dr,dc in directions:

                    nr,nc = dr+r,dc+c
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0):
                        continue
                    
                    grid[nr][nc] = 0
                    q.append((nr,nc))
                    area += 1
            
            return area

        for r in range(rows):
                for c in range(cols):

                    if grid[r][c] == 1:
                        max_area = max(max_area,bfs(r,c))
        
        return max_area
            



        