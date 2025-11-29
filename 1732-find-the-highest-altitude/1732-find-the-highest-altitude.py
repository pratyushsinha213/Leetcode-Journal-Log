class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start = 0
        highest = 0
        for i in range(len(gain)):
            start += gain[i]
            highest = max(highest, start)

        return highest