class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        word_frequency = [(-freq, word) for word, freq in counter.items()]

        heapq.heapify(word_frequency)

        arr = []
        for i in range(k):
            most_freq, word = heapq.heappop(word_frequency)
            arr.append(word)
        
        return arr