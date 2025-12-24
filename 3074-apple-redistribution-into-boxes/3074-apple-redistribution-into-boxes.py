class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)

        capacity.sort(reverse=True)

        cnt_boxes = 0
        while total > 0:
            total -= capacity[cnt_boxes]
            cnt_boxes += 1

        return cnt_boxes