class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_arr = [1] * len(nums)
        right_arr =[1] * len(nums)

        for i in range(len(nums)-1):
            left_arr[i+1] = left_arr[i] * nums[i] # [1,1, 2,8]
        for j in reversed(range(1, len(nums))):
            right_arr[j-1] = right_arr[j] * nums[j] #[48,24,6,1]
        
        
        output = [0] * len(nums)
        for k in range(len(nums)):
            output[k] = left_arr[k] * right_arr[k]
             
        return output
        
