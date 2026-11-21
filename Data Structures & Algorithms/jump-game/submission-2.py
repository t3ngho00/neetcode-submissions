class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1
        visit = {i:-1 for i in range(len(nums))}
        def helper(i):
            if i>end:
                return 0
            if visit[i] != -1:
                return visit[i]
            if i == end:
                return 1
            if nums[i] == 0:
                return 0
            res = 0
            for n in range(1,nums[i]+1):
                res+= helper(i+n)
            visit[i] = res
            return res
        result = helper(0)
        if result != 0: return True
        return False
            