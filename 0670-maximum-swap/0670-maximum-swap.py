class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        num_sorted = sorted(num, reverse=True)
        i = 0
        swap = False
        while i < len(num_sorted):
            if num_sorted[i] > num[i]:
                tmp = num[i]
                num[i] = num_sorted[i]
                swap = True
                break
            i += 1
        if swap:
            index = -list(reversed(num)).index(num_sorted[i])-1
            num[index] = tmp
        return int("".join(i for i in num))
