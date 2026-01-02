class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rotation = k % (m * n)

        # Flatten grid
        flat = []
        for row in grid:
            flat.extend(row)

        # Rotate right by k
        flat = flat[-rotation:] + flat[:-rotation]

        # Rebuild grid
        res = [[0] * n for _ in range(m)]
        idx = 0
        for i in range(m):
            for j in range(n):
                res[i][j] = flat[idx]
                idx += 1

        return res