class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        for i in range(32):
            tmp = n>>i & 1
            rev = rev | (tmp<<(31-i))
        return rev