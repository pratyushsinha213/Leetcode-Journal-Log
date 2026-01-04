class Solution:
    def sortSentence(self, s: str) -> str:
        order = dict()
        s_arr = s.split(" ")
        
        for word in s_arr:
            ext_word, o = word[:len(word)-1], word[-1]
            order[int(o)] = ext_word
            print(order)

        sorted_order = sorted(order.keys())
        print(sorted_order)
        
        res = []
        for o in sorted_order:
            res.append(order[o])
        
        return ' '.join(res)