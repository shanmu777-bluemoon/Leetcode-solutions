class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If only one row or string is too short, no zigzag is possible
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of strings, one for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False

        for char in s:
            # Add character to the current row
            rows[current_row] += char
            
            # If we hit the top or bottom row, reverse the direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move up or down based on the direction flag
            current_row += 1 if going_down else -1

        # Join all row strings together to get the final result
        return "".join(rows)
