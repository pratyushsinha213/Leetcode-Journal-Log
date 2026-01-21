class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_num = 0
        rev = columnTitle[::-1]
        
        for i in range(len(rev)):
            col_num += (26**i * (ord(rev[i]) - ord('A') + 1))

        return col_num