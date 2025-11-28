class Solution:
    def isThree(self, n: int) -> bool:
        k = 0

        result = []
        for i in range(1, n+1):
            if n % i == 0:
                result.append(i)
                if len(result) > 3:
                    return False
        
        return False if len(result) != 3 else True