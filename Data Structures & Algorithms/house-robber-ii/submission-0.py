class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        elif len(nums) ==1:
            return nums[0]
        
        def helper(houses):
            if len(houses) == 0 :
                return 0
            elif len(houses) ==1:
                return houses[0]
            else:
                dp = [0] * len(houses)
                dp[0],dp[1] = houses[0], max(houses[0], houses[1])
                i = 2
                while i < len(houses):
                    dp[i] = max(dp[i-1], ( houses[i]+ dp[i-2]))
                    i+=1
                return dp[-1]
        return max(helper(nums[:-1]), helper(nums[1:]))
