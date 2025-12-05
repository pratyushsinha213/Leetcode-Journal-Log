class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        arr = []
        for num, count in counter.items():
            if count > 1:
                arr.append(num)
                
        return arr