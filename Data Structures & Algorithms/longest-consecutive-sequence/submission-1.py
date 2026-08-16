class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        longest = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in arr:
                length = 0
                while (nums[i] + length) in arr:
                    length += 1

                longest = max(longest, length)
        return longest

        