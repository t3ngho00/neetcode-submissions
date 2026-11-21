class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        inorder = [num for num in nums]
        reverse = [num for num in nums]
        result = [1] * len(nums)

        for i in range(1, len(nums)):
            inorder[i] *= inorder[i - 1]

        for j in range(len(nums) - 2, -1, -1):
            reverse[j] *= reverse[j + 1]

        result[0] = reverse[1]
        result[-1] = inorder[-2]

        for k in range(1, len(nums) - 1):
            result[k] = inorder[k - 1] * reverse[k + 1]

        return result