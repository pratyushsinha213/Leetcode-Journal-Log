class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start = 0
        highest = 0
        for alt in gain:
            start += alt
            highest = max(highest, start)

        return highest