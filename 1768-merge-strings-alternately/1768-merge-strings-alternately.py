class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        if (len(word1) == len(word2)):
            for i in range(len(word1)):
                result += (word1[i]+word2[i])
            return result

        i = 0
        while (i < len(word1) and i < len(word2)):
            result += (word1[i]+word2[i])
            i += 1
            if (i == len(word1)):
                result += word2[i:]
                return result
            elif (i == len(word2)):
                result += word1[i:]
                return result