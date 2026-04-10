from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            # Base Case: If we reached the end of the pattern
            if j == len(p):
                return i == len(s)
            
            # Check if current characters match
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            # Handle the '*' wildcard
            if (j + 1) < len(p) and p[j + 1] == '*':
                # Choice 1: Skip the '*' and its preceding character (match 0 times)
                # Choice 2: If there's a match, consume one char from 's' and stay on '*'
                return dfs(i, j + 2) or (match and dfs(i + 1, j))
            
            # Standard match: move both pointers forward
            if match:
                return dfs(i + 1, j + 1)
            
            return False
            
        return dfs(0, 0)
