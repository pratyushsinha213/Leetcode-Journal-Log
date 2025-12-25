class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # h = [-i for i in happiness]
        # heapify(h)

        # happiness_count = 0
        # while k > 0:
        #     child = heappop(h) * -1
        #     happiness_count += child
        #     for i in range(len(h)):
        #         if h[i] < 0:
        #             h[i] += 1
        #     k -= 1
        
        # return happiness_count

        happiness.sort()
        count = 0
        res = 0

        for i in range(len(happiness)-1, len(happiness)-k-1, -1):
            if happiness[i]-count > 0:
                res += (happiness[i]-count)
            count += 1

        return res