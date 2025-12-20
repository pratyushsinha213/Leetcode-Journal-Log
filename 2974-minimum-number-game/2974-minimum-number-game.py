class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapify(nums)
        arr = []
        while nums:
            alice = heappop(nums)
            bob = heappop(nums)
            arr.extend([bob, alice])

        return arr