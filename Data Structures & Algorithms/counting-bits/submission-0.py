class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * n
        result = [0]
        offset = 1
        for i in range(1, n+1):
            if i == offset:
                offset*=2
            result.append(result[i-offset]+1)
        return result
        