from collections import Counter
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alp = [0] * 26
        counter = Counter(sentence)

        for alphabet, occ in counter.items():
            alp[ord(alphabet)-ord('a')] += occ
        

        return 0 not in alp