class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s = set(list(range(left, right+1)))
        arr = []
        for num in range(left, right+1):
            for l_range, r_range in ranges:
                if l_range <= num <= r_range:
                    break
            else:
                return False
        
        return True