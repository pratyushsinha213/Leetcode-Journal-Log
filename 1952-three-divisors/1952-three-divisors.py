class Solution:
    def isThree(self, n: int) -> bool:
        result = []
        for i in range(1, n+1):
            if n % i == 0:
                result.append(i)
                if len(result) > 3:
                    return False
        
        return len(result) == 3