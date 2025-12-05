class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        moves = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }

        x, y = 0, 0

        for command in commands:
            dx, dy = moves[command]
            x = x + dx
            y = y + dy

        return x * n + y