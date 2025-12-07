class Solution:
    def removeZeros(self, n: int) -> int:
        str_n = str(n)

        builder = ''
        for number in str_n:
            if number != '0':
                builder += number

        return int(builder)