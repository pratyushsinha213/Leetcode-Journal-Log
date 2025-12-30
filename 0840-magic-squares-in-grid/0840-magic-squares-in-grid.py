class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:        
        def is_magic_square(row, col):
            _1 = grid[row][col]
            _2 = grid[row][col+1]
            _3 = grid[row][col+2]
            
            _4 = grid[row+1][col]
            _5 = grid[row+1][col+1]
            _6 = grid[row+1][col+2]
            
            _7 = grid[row+2][col]
            _8 = grid[row+2][col+1]
            _9 = grid[row+2][col+2]

            if({_1, _2, _3, _4, _5, _6, _7, _8, _9} == s):
                if((_1 + _2 + _3) == (_4 + _5 + _6) == (_7 + _8 + _9) == (_1 + _4 + _7) == (_2 + _5 + _8) == (_3 + _6 + _9) == (_1 + _5 + _9) == (_3 + _5 + _7)):
                    return True
        
            return False

        m, n = len(grid), len(grid[0])
        count = 0
        s = set(list(range(1, 10)))
        for i in range(m-2):
            for j in range(n-2):
                if is_magic_square(i, j):
                    count += 1

        return count