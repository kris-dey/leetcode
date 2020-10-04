class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = x * sign
        rev = 0
        while x > 0:
            tmp = x % 10
            x = x // 10
            rev = rev*10 + tmp
            
        if rev > 2**31 - 1 or rev < -2**31:
            return 0

        return rev * sign