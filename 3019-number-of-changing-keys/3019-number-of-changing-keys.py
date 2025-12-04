class Solution:
    def countKeyChanges(self, s: str) -> int:
        change = 0

        for i in range(len(s)-1):
            if abs(ord(s[i]) - ord(s[i+1])) != 32 and abs(ord(s[i]) - ord(s[i+1])) != 0:
                change += 1
        
        return change
        # print(f"a: {ord('a')}, A: {ord('A')}, diff: {ord('a')-ord('A')}")
        # print(f"b: {ord('b')}, B: {ord('B')}, diff: {ord('b')-ord('B')}")