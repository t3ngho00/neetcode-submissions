class Solution:
    def findMin(self, nums: list[int]) -> int:
        def helper(l, r):
            if l == r:
                return nums[l]

            if nums[l] <= nums[r]:
                return nums[l]

            mid = (l + r) // 2

            if nums[l] > nums[mid]:
                return helper(l, mid)

            return helper(mid + 1, r)

        return helper(0, len(nums) - 1)