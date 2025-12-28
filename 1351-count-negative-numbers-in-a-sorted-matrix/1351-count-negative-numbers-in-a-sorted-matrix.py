class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # T : O(n^2)
        # count = 0
        
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j] < 0:
        #             count += 1

        # return count

        m, n = len(grid), len(grid[0])
        i, j = 0, n-1

        count = 0
        while j >= 0 and i < m:
            if grid[i][j] < 0:
                count += (m-i)
                j -= 1
            else:
                i += 1

        return count