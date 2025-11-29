class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        char_map = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

        final_pos = (char_map[coordinates[0]], int(coordinates[1]))

        if (final_pos[0] % 2 == 1 and final_pos[1] % 2 == 1) or (final_pos[0] % 2 == 0 and final_pos[1] % 2 == 0):
            return False
        else:
            return True