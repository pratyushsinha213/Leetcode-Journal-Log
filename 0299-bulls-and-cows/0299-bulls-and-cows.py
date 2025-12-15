class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count_bulls = count_cows = 0
        counter = [0] * 10
        for i in range(len(secret)):
            counter[int(secret[i])] += 1
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                count_bulls += 1
                counter[int(secret[i])] -= 1
        
        for i in range(len(secret)):
            if secret[i] != guess[i]:
                d = int(guess[i])
                if counter[d] > 0:
                    count_cows += 1
                    counter[d] -= 1

        result = f"{count_bulls}A{count_cows}B"
        return result