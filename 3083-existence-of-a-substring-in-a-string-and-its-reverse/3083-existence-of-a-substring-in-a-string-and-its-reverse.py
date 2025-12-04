class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        # Method 1

        # for i in range(len(s)):
        #     for j in range(i+1, len(s)):
        #         sub_str = s[i:j+1]
        #         if sub_str[::-1] in s:
        #             return True
                
        # return False

        for i in range(len(s)-1):
            sub_str = s[i:i+2]
            if sub_str[::-1] in s:
                return True
        
        return False