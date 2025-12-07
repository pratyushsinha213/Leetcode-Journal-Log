class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)

        total = 0
        for num, count in counter.items():
            if count % k == 0:
                total += (num * count)
            
        return total