class Solution:
    def reverseVowels(self, s: str) -> str:
        # arr = [char for char in s]
        # vowels = []
        # vowelString = 'aeiouAEIOU'

        # for i in range(len(arr)):
        #     if (arr[i] in vowelString):
        #         vowels.append(arr[i])
        #         arr[i] = 'inf'
        
        # reverse = vowels[::-1]
        # j = 0
        # for i in range(len(arr)):
        #     if (arr[i] == 'inf' and j < len(reverse)):
        #         arr[i] = reverse[j]
        #         j += 1

        # return ''.join(arr)
        
        word = list(s)
        start = 0
        end = len(s) - 1
        vowels = "aeiouAEIOU"

        while start < end:
            while start < end and word[start] not in vowels:
                start += 1
            while start < end and word[end] not in vowels:
                end -= 1

            # Swap vowels
            word[start], word[end] = word[end], word[start]

            start += 1
            end -= 1

        return ''.join(word)