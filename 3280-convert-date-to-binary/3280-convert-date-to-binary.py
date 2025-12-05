class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split('-')
        print(year, month, day)

        bin_rep = f"{bin(int(year))[2:]}-{bin(int(month))[2:]}-{bin(int(day))[2:]}" 

        return bin_rep