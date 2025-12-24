class Solution:
    def countTime(self, time: str) -> int:
        h = time[:2]
        s = time[3:]
        psblty = 1

        if h == "??":
            psblty *= 24
        else:
            # Check the first hour number
            if h[0] == "?":
                # Check if second hour number > 3 
                if int(h[1]) > 3:
                    psblty *= 2
                else:
                    psblty *= 3

            if h[1] == "?":
                if int(h[0]) < 2:
                    psblty *= 10
                else:
                    # 2?(0123):00
                    psblty *= 4

        if s[0] == "?":
            psblty *= 6
        if s[1] == "?":
            psblty *= 10

        return psblty