class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        first, second = 0, 0
        for i in range(len(cost)-1, -1, -1):
            minimum = cost[i] + min(first,second)
            first = second
            second = minimum
        return min(first, second)
        