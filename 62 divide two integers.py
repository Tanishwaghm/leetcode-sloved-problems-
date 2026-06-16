class Solution(object):
    def divide(self, dividend, divisor):

        # Edge case overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle sign
        negative = (dividend < 0) != (divisor < 0)

        # Convert to positive
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:

            temp = divisor
            multiple = 1

            # Double divisor until it is just smaller than dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            result += multiple

        if negative:
            result = -result

        # clamp result
        return min(max(result, INT_MIN), INT_MAX)
