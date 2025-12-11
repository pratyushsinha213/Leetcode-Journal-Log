class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        total_len = 0
        for word in words:
            word_counter = Counter(word)

            if word_counter <= counter:
                total_len += len(word)
        
        return total_len