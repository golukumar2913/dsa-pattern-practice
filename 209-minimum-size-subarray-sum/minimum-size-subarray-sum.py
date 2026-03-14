class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        sum_sub = 0
        min_len = float('inf')

        for high in range(n):
            sum_sub += nums[high]

            while sum_sub >= target:
                length = high - low + 1
                min_len = min(min_len, length)

                sum_sub -= nums[low]
                low += 1

        if min_len == float('inf'):
            return 0

        return min_len

