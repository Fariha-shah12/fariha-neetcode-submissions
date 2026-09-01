class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp= [0] * (len(nums))
        max_sum = nums[0]
        dp[0] = nums[0]
        i =0
        best_start, best_end, start = 0,0,0

        if len(nums)> 1:
            while i +1 <= len(nums):
                dp[i] = max(dp[i-1] + nums[i], nums[i])
                max_sum = max(max_sum, dp[i])
                i+=1
        return max_sum