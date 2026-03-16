class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        feq = {}
        max_feq = 0 
        res = 0

        for right in range(len(s)):
            feq[s[right]] = feq.get(s[right], 0) +1
            max_feq = max(max_feq , feq[s[right]]) 

            while (right - left +  1) - max_feq > k:
                feq[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)


        return res
