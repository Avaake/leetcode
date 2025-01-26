class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number = 0
        for char in columnTitle:
            column_number = column_number * 26 + ord(char) - ord('A') + 1
        return column_number
