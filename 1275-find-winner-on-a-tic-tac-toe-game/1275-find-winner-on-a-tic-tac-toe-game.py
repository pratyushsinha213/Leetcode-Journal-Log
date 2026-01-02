class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def winner(arr):
            _1 = arr[0][0]
            _2 = arr[0][1]
            _3 = arr[0][2]

            _4 = arr[1][0]
            _5 = arr[1][1]
            _6 = arr[1][2]
            
            _7 = arr[2][0]
            _8 = arr[2][1]
            _9 = arr[2][2]

            if ((_1 == 'X' and _2 == 'X' and _3 == 'X') or (_4 == 'X' and _5 == 'X' and _6 == 'X') or (_7 == 'X' and _8 == 'X' and _9 == 'X') or (_1 == 'X' and _4 == 'X' and _7 == 'X') or (_2 == 'X' and _5 == 'X' and _8 == 'X') or (_3 == 'X' and _6 == 'X' and _9 == 'X') or (_1 == 'X' and _5 == 'X' and _9 == 'X') or (_3 == 'X' and _5 == 'X' and _7 == 'X')):
                return "A"
            elif ((_1 == 'O' and _2 == 'O' and _3 == 'O') or (_4 == 'O' and _5 == 'O' and _6 == 'O') or (_7 == 'O' and _8 == 'O' and _9 == 'O') or (_1 == 'O' and _4 == 'O' and _7 == 'O') or (_2 == 'O' and _5 == 'O' and _8 == 'O') or (_3 == 'O' and _6 == 'O' and _9 == 'O') or (_1 == 'O' and _5 == 'O' and _9 == 'O') or (_3 == 'O' and _5 == 'O' and _7 == 'O')):
                return "B"
            elif (_1 == None or _2 == None or _3 == None or _4 == None or _5 == None or _6 == None or _7 == None or _8 == None or _9 == None):
                return "Pending"
            else:
                return "Draw"

        grid = [[None] * 3 for _ in range(3)]

        for player_a in range(0, len(moves), 2):
            i, j = moves[player_a]
            grid[i][j] = "X"
        
        for player_b in range(1, len(moves), 2):
            i, j = moves[player_b]
            grid[i][j] = "O"
        
        for i in range(3):
            for j in range(3):
                if grid[i][j] == None:
                    print("-", end=" ")
                else:
                    print(grid[i][j], end=" ")
            print()
            
        return winner(grid)