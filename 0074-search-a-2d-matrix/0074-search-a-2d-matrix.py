class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            minn, maxx = min(matrix[i]), max(matrix[i])
            if target < minn or target > maxx:
                continue
            else:
                for j in range(n):
                    if matrix[i][j] == target:
                        return True
            
        return False