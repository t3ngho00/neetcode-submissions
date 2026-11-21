class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashM = {} # num: freq
        freq = [[] for _ in range(len(nums)+1)]
        for num in nums:
            hashM[num] = 1 + hashM.get(num, 0)
        for num, count in hashM.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
