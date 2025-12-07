class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minn, maxx = min(nums), max(nums)

        arr = []
        for i in range(minn, maxx+1):
            if i not in nums:
                arr.append(i)
        return arr