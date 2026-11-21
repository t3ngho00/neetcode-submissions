class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1
        goal = end
        i = end
        while i>=0:           
            if nums[i] + i >= goal:
                goal = i
            i-=1
            if goal == 0:
                return True
        return False