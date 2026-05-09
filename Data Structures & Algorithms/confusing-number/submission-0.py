class Solution:
    def confusingNumber(self, n: int) -> bool:
        invert_map = {0:0, 1:1, 8:8, 6:9, 9:6}
        invert_number = 0
        n_copy = n

        while n_copy:
            result = n_copy % 10
            if result not in invert_map:
                return False

            invert_number = invert_number * 10 + invert_map[result]
            n_copy //= 10

        return invert_number != n