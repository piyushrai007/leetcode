class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        invert_count = 0
        len = (1 << n) - 1  # Length of Sn is 2^n - 1

        while k > 1:
            # If k is in the middle, return based on inversion count
            if k == len // 2 + 1:
                return "1" if invert_count % 2 == 0 else "0"

            # If k is in the second half, invert and mirror
            if k > len // 2:
                k = len + 1 - k  # Mirror position
                invert_count += 1  # Increment inversion count

            len //= 2  # Reduce length for next iteration

        # For the first position, return based on inversion count
        return "0" if invert_count % 2 == 0 else "1"