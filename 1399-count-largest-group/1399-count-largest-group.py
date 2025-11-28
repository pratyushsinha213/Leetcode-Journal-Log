class Solution:
    def countLargestGroup(self, n: int) -> int:
        counter = dict()
        
        for i in range(1, n+1):
            add = sum([int(num) for num in str(i)])
            # print(i, add)
            if add not in counter.keys():
                counter[add] = [i]
            else:
                counter[add].append(i)

        result = [arr for arr in counter.values()]
        size = [len(arr) for arr in result]
        
        return size.count(max(size))