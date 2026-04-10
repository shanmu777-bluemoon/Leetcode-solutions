class Solution:
    def myAtoi(self, s: str) -> int:
        # Define constants for 32-bit signed integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # 1. Skip leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        # 2. Check for optional sign
        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index = 1
        elif s[0] == '+':
            index = 1
        
        # 3. Read digits and convert
        res = 0
        while index < len(s) and s[index].isdigit():
            res = res * 10 + int(s[index])
            index += 1
            
            # 4. Handle overflow early to avoid huge numbers
            if sign * res > INT_MAX:
                return INT_MAX
            if sign * res < INT_MIN:
                return INT_MIN
        
        return sign * res
