class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cons_count = 2

        i = 0
        while i < len(arr)-1:
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1:
                cons_count -= 1
                if cons_count == 0:
                    return True
            else:
                cons_count = 2
            i += 1
        return False