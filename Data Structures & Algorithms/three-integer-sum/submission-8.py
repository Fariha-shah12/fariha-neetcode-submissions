from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        count = defaultdict(int)
        for i in range(len(nums)):
            left = i+1
            right = (len(nums)-1)
            target= -(nums[i])
            while left < right:
                if nums[left] + nums[right]< target:
                    left +=1
                elif  nums[left] + nums[right]  > target:
                    right-=1
                else:
                  
                    triplet = (nums[i], nums[left], nums[right])
                    if count[triplet] == 0:
                        res.append(list(triplet))
                        count[triplet] += 1
                    
                    left +=1
                    right-=1
        return res