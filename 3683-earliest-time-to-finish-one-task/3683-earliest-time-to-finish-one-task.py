class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        arr = []
        for start, end in tasks:
            time = start + end
            arr.append(time)
        
        return min(arr)