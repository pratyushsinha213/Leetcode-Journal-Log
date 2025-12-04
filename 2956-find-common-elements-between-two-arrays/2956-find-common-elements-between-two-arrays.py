class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer1, answer2 = 0, 0
        set_1, set_2 = set(nums1), set(nums2)
        
        for i in range(len(nums1)):
            if nums1[i] in set_2:
                answer1 += 1

        for i in range(len(nums2)):
            if nums2[i] in set_1:
                answer2 += 1
        
        return [answer1, answer2]