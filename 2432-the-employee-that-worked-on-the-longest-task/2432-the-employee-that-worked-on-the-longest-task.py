class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_time = logs[0][1]
        emp = logs[0][0]

        for i in range(1, len(logs)):
            duration = logs[i][1] - logs[i-1][1]
            if duration > max_time or (duration == max_time and logs[i][0] < emp):
                max_time = duration
                emp = logs[i][0]

        return emp