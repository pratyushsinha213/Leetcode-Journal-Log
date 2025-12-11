class Solution:
    def defangIPaddr(self, address: str) -> str:
        str_builder = ""

        for i in range(len(address)):
            if address[i] == '.':
                str_builder += '[.]'
            else:
                str_builder += address[i]

        return str_builder