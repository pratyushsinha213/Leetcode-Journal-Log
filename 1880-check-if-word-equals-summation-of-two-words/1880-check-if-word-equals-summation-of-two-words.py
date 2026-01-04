class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        n_firstword = ''.join([str(ord(ch)-ord('a')) for ch in firstWord])     
        n_secondword = ''.join([str(ord(ch)-ord('a')) for ch in secondWord])     
        n_targetword = ''.join([str(ord(ch)-ord('a')) for ch in targetWord])     
        

        return int(n_firstword) + int(n_secondword) == int(n_targetword)