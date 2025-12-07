class Solution:
    def minimumFlips(self, n: int) -> int:
        bin_n = bin(n)[2:]

        rev = bin_n[::-1]

        if bin_n == rev:
            return 0
        
        result = 0
        for i in range(len(rev)):
            if (bin_n[i] == "1" and rev[i] == "0") or (bin_n[i] == "0" and rev[i] == "1"):
                result += 1
            
        return result