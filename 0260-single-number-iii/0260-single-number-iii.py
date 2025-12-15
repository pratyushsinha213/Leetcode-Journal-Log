class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # counter = Counter(nums)
        # for num, count in counter.items():
        #     if count == 1:
        #         arr.append()

        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
            
        return list(seen)