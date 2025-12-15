class Solution:
    def bulbSwitch(self, n: int) -> int:
        # state = [False] * n

        # if n <= 1:
        #     return n
        
        # for i in range(1, n+1):
        #     for j in range(i - 1, n, i):
        #         state[j] = not state[j]
        #     # print(i, state)

        # return state.count(True)

        return int(n ** 0.5)