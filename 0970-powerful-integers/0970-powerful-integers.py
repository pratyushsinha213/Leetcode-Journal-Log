class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        arr = set()

        for i in range(30):
            for j in range(30):
                integer = x**i + y**j
                if integer <= bound:
                    arr.add(integer)
        
        return sorted(list(arr))