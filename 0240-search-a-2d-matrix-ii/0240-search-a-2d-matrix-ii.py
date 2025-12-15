class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            min_elem, max_elem = matrix[i][0], matrix[i][-1]
            if min_elem <= target <= max_elem:
                for j in range(n):
                    if target == matrix[i][j]:
                        return True

        return False