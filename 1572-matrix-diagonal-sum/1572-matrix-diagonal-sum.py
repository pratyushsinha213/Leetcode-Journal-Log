class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat) == 1:
            return mat[0][0]
        
        m, n = len(mat), len(mat[0])
        total = 0
        seen = set()
        for i in range(m):
            for j in range(n):
                if i == j and (i, j) not in seen:
                    total += mat[i][j]
                    seen.add((i, j))
                elif i + j == m-1 and (i, j) not in seen:
                    total += mat[i][j]
                    seen.add((i, j))
        return total