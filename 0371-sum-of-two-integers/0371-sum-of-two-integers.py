class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 음수 처리를 위한 32비트 마스크 사용
        MASK = 0xFFFFFFFF
        MAX = 0x7FFFFFFF
        
        while b!=0:
            a, b = (a^b)&MASK, ((a&b)<<1)&MASK
        return a if a<= MAX else ~(a^MASK)