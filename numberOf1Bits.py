class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        for i in range(32):
            if n >> i & 1 == 1:
                counter = counter + 1
                
        return counter