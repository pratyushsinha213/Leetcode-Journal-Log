class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substr = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if (i == j):
                    continue
                if (words[i] in words[j]):
                    substr.add(words[i])

        return list(substr)