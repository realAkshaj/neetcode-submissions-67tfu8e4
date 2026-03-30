class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        rows,cols = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(grid,r,c,visit):
             
            if (min(r,c) < 0 or r == rows or c == cols or grid[r][c] == 1 or (r,c) in visit):
                return 0           

            
            if r == rows - 1 and c == cols - 1:
                return 1

            visit.add((r,c))

            count = 0
            for dr,dc in directions:
                
                new_row,new_col = r+dr, c+dc

                count += dfs(grid,new_row,new_col,visit)
            
            visit.remove((r,c))
            return count
        
        return dfs(grid,0,0,set())



        