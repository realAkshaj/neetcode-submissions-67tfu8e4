class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        r,c = len(matrix),len(matrix[0])

        left,right = 0, r*c-1
        while left <= right:

            m = (left + right) // 2
            row,col = m//c, m % c
            if target > matrix[row][col]:                
                left = m + 1
            elif target < matrix[row][col]:
                right = m - 1
            else:
                return True
        return False