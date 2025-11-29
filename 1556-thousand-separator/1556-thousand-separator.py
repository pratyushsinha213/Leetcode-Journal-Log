class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        str_builder = ""
        count = 0
        
        for i in range(len(s) - 1, -1, -1):
            str_builder += s[i]
            count += 1
            if count == 3 and i != 0:
                str_builder += '.'
                count = 0
        
        return str_builder[::-1]