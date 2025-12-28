class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # T : O(n^2)
        # count = 0
        
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j] < 0:
        #             count += 1

        # return count

        arr = []

        for row in grid:
            arr.extend(row)

        count = 0
        for elem in arr:
            if elem < 0:
                count += 1
        
        return count