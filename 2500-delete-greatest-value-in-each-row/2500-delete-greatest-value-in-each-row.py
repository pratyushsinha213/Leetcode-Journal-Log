class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        pqs = []
        for row in grid:
            pq = [v * -1 for v in row]
            heapify(pq)
            pqs.append(pq)
        
        count = 0
        while any(pqs):
            vals = []
            for pq in pqs:
                vals.append(heappop(pq) * -1)
            count += max(vals)

        return count