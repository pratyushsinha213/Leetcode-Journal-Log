class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    valid = True

                    # Check row i
                    for col in range(n):
                        if mat[i][col] == 1 and col != j:
                            valid = False
                            break
                    
                    # Check column j
                    if valid:
                        for row in range(m):
                            if mat[row][j] == 1 and row != i:
                                valid = False
                                break
                    
                    if valid:
                        count += 1

        return count