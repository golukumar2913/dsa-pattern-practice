class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        max_diff = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)-2):
            
            j = i + 1
            k = len(nums) -1

            while j < k:
                total = nums[i] + nums[j]+ nums[k]
                

                if abs(target - total) < abs(target - max_diff):
                    max_diff = total

                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    return total

        return max_diff                




    