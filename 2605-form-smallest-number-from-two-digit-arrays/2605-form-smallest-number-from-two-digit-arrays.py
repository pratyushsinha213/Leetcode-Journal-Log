class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1) & set(nums2)
        if common:
            return min(common)

        minn_1, minn_2 = min(nums1), min(nums2)
        if minn_1 < minn_2:
            return int(str(minn_1) + str(minn_2))
        elif minn_2 < minn_1:
            return int(str(minn_2) + str(minn_1))
            