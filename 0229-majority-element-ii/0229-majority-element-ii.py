class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums

        occurence = floor(n/3)
        counter = Counter(nums)
        arr = []

        for num, count in counter.items():
            if count > occurence:
                arr.append(num)

        return arr