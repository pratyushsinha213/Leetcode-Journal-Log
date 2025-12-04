class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        # Condition 1: Column values must be identical top to bottom
        for i in range(m - 1):
            for j in range(n):
                if grid[i][j] != grid[i+1][j]:
                    return False

        # Condition 2: Adjacent values in each row must be different
        for i in range(m):
            for j in range(n - 1):
                if grid[i][j] == grid[i][j+1]:
                    return False

        return True