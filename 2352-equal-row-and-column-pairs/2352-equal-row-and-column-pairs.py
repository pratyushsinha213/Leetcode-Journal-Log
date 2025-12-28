# class Solution:
#     def equalPairs(self, grid: List[List[int]]) -> int:
#         rows = dict()
#         cols = dict()

#         n = len(grid)

#         # First appending rows
#         for i in range(n):
#             t = tuple(grid[i])
#             if t in rows:
#                 rows[t] += 1
#             else:
#                 rows[t] = 1

#         # Appending Columns:
#         for i in range(n):
#             temp = []
#             for j in range(n):
#                 temp.append(grid[j][i])
#             t = tuple(temp)
#             if t in cols:
#                 cols[t] += 1
#             else:
#                 cols[t] = 1

#         print(rows, cols)

from collections import Counter
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Count rows
        row_counter = Counter(tuple(row) for row in grid)

        count = 0
        # Build each column and check matches
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            count += row_counter[col]

        return count