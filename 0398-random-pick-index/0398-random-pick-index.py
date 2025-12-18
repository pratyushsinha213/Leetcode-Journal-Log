class Solution:

    def __init__(self, nums: List[int]):
        self.hash = {}
        for i in range(len(nums)):
            if nums[i] in self.hash:
                self.hash[nums[i]].append(i)
            else:
                self.hash[nums[i]] = [i]

    def pick(self, target: int) -> int:
        return random.choice(self.hash[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)