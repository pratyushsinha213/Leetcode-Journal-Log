class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split(" ")
        arr = []
        for i in range(len(words)-2):
            if words[i] == first and words[i+1] == second:
                arr.append(words[i+2])

        return arr