class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False
        
        # count = 0
        # pile = 10

        # while n >= pile:
        #     n -= pile
        #     pile -= 1
        #     count += 1

        # return count % 2 != 0

        first = 10
        isAlice = True
        while n > 0:
            if first > n:
                return not isAlice

            n -= first
            first -= 1
            isAlice = not isAlice

        return not isAlice