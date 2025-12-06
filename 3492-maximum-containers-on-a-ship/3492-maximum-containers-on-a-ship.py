class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        grid_size = n * n                       # total slots
        weight_limit = maxWeight // w           # how many containers weight allows
        
        return min(grid_size, weight_limit)