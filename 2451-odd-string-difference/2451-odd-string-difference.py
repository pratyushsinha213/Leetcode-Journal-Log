class Solution:
    def oddString(self, words: List[str]) -> str:
        patterns = []
        for word in words:
            # arr = [0] * 26
            # for i in range(len(word)):
            #     arr[ord(word[i])-ord('a')] += 1
            
            # diff = [] 
            # for j in range(len(arr)):
            #     if arr[j] == 1:
            #         diff.append(j)
            n = len(word)
            diff = []
            for i in range(n-1):
                difference = (ord(word[i+1])-ord('a')) - (ord(word[i])-ord('a'))
                diff.append(difference)
            
            patterns.append(diff)

        
        for idx, ptrn in enumerate(patterns):
            if patterns.count(ptrn) == 1:
                return words[idx]