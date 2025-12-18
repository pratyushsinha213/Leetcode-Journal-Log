class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s = set()
        arr = []
        for num in nums:
            if num in s:
                s.remove(num)
                arr.append(num)
            else:
                s.add(num)

        return arr