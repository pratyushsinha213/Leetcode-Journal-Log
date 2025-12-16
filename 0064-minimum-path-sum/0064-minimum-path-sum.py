class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return grid[-1][-1]
            
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        # First Row
        for i in range(1, n):
            # print(grid[0][i])
            # dp[0][i] = sum(grid[0][:i+1])
            dp[0][i] = dp[0][i-1] + grid[0][i]
        
        #  First Col
        for j in range(1, m):
            # print(grid[:j+1][0])
            dp[j][0] = dp[j-1][0] + grid[j][0]
        
        # Rest Rows
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
        
        return dp[-1][-1]