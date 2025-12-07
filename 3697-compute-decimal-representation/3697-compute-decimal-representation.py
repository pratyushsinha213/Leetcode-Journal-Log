class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        rep = []
        str_n = str(n)

        for i in range(len(str_n)):
            num = str_n[i] + '0' * (len(str_n)-1-i)
            if int(num) != 0:
                rep.append(int(num))
        
        return rep