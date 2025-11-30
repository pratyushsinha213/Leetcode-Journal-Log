class Solution:
    def checkString(self, s: str) -> bool:
        if 'a' not in s or 'ba' not in s:
            return True
        
        return False