class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)

        res = 0
        while x != 0:
            pop = x % 10
            x //= 10
            res = res*10 + pop
        if is_negative:
            res *= -1

        return res if -2**31 <= res <= 2**31 - 1 else 0      