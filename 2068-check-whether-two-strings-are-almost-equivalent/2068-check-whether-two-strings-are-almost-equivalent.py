from collections import Counter
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter_word1 = Counter(word1)
        counter_word2 = Counter(word2)

        print(counter_word1, counter_word2)

        for letter, count in counter_word2.items():
            print(counter_word1[letter], counter_word2[letter])
            if abs(counter_word1[letter] - counter_word2[letter]) > 3:
                return False

        for letter, count in counter_word1.items():
            print(counter_word1[letter], counter_word2[letter])
            if abs(counter_word1[letter] - counter_word2[letter]) > 3:
                return False

        return True