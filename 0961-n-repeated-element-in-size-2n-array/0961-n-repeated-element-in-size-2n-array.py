class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        c = Counter(nums)
        _2n = len(nums)
        n = _2n//2

        for num, count in c.items():
            if count == n:
                return num