class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)>1:
            dp = [0] * len(nums)
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            i = 2
            while i < len(nums):
                dp[i] = max(dp[i-1], ( nums[i]+ dp[i-2]))
                i+=1
            return (dp[-1])
        elif len(nums) ==1:
            return nums[0]
        else: 
            return [0]

        

            
        