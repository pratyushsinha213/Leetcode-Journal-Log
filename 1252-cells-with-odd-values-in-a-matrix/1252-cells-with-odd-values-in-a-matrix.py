class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        arr = [[0] * n for _ in range(m)]
        
        for index in indices:
            i, j = index

            # row increment
            for row in range(m):
                arr[row][j] += 1
            
            # col increment
            for col in range(n):
                arr[i][col] += 1

        odd_occ = 0
        for i in range(m):
            for j in range(n):
                if arr[i][j] % 2 != 0:
                    odd_occ += 1
        
        return odd_occ