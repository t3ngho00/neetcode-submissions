class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        starting = []
        for num in uniqueNums:
            if num-1 not in uniqueNums:
                starting.append(num)
        result = 0
        for num in starting:
            cur_max = 1
            cur_num = num
            while cur_num + 1 in uniqueNums:
                cur_max += 1
                cur_num += 1
            result = max(result, cur_max)
        return result
            
