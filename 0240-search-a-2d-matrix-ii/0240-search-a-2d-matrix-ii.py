class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s, e = 0, len(matrix[0])
        for r in range(len(matrix)):
            for c in range(s, e):
                if matrix[r][c]==target:
                    return True
                if matrix[r][c]>target:
                    e = c
                    break
        return False
