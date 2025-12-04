class Solution:
    def averageValue(self, nums: List[int]) -> int:
        avg_l = []
        for num in nums:
            if num % 3 == 0 and num % 2 == 0:
                avg_l.append(num)
            
        return int(sum(avg_l)/len(avg_l)) if len(avg_l) != 0 else 0