class Solution:
    def bestClosingTime(self, customers: str) -> int:
        best_time = min_penalty = prefix_sum = 0

        for i in range(len(customers)):
            prefix_sum += -1 if customers[i] == 'Y' else 1

            if prefix_sum < min_penalty:
                best_time = i+1
                min_penalty = prefix_sum

        return best_time