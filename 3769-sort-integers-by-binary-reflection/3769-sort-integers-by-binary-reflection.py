class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        array = []
        for num in nums:
            rev_bin = bin(num)[2:][::-1]
            reverse = int(rev_bin, 2)

            array.append((reverse, num))
        
        array.sort()

        return [n for _, n in array]