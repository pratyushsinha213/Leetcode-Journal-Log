class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # gifts = [-gift for gift in gifts]

        # heapify(gifts)

        for i in range(k):
            gift = max(gifts)
            idx = gifts.index(gift)
            root = int(sqrt(gift))
            gifts[idx] = root

        return sum(gifts)