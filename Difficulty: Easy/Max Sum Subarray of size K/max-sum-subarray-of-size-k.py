class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)

        low = 0
        high = k - 1
        sum_sub = 0
        res = 0

        for i in range(low, high + 1):
            sum_sub += arr[i]

        while high < n:
            res = max(res, sum_sub)

            low += 1
            high += 1

            if high == n:
                break

            sum_sub -= arr[low - 1]
            sum_sub += arr[high]

        return res
