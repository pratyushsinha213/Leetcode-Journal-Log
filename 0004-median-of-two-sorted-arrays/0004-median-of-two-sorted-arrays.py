class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_sorted = sorted(nums1 + nums2)
        n = len(merged_sorted)

        if n % 2 == 0:
            return (merged_sorted[n // 2 - 1] + merged_sorted[n // 2]) / 2
        else:
            return merged_sorted[n // 2]