class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat) == 1:
            return mat[0][0]
        
        m, n = len(mat), len(mat[0])
        total = 0
        for i in range(m):
            for j in range(n):
                if i == j or i + j == m-1:
                    total += mat[i][j]
        return total