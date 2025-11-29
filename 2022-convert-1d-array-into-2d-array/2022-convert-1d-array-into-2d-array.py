class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []

        two_dim_arr = [[0 for _ in range(n)] for _ in range(m)]

        idx = 0
        for i in range(m):
            for j in range(n):
                two_dim_arr[i][j] = original[idx]
                idx += 1
        
        return two_dim_arr