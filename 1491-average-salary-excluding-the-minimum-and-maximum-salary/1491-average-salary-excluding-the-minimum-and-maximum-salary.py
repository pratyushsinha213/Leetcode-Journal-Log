class Solution:
    def average(self, salary: List[int]) -> float:
        number = 0
        runn_sum = 0
        min_sal, max_sal = min(salary), max(salary)

        for s in salary:
            if s != max_sal and s != min_sal:
                runn_sum += s
                number += 1
        
        return (runn_sum/number)