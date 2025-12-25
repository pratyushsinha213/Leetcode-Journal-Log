class Solution:
    def reverseWords(self, s: str) -> str:
        reverseWord = [x for x in s.split()][::-1]
        result = ''
        for i in range(len(reverseWord)):
            if (i != len(reverseWord)-1):
                result += (reverseWord[i] + ' ')
            else:
                result += reverseWord[i]

        return result 