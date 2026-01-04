class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # if s == "1":
        #     return True
        # if s == "0":
        #     return False

        # for i in range(len(s)-1):
        #     if s[i] == '0' and s[i+1] == '1':
        #         return False

        # return True

        return "01" not in s