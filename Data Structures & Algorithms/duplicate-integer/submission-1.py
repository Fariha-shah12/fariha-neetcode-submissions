class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = False
        count = Counter(nums)
        for i in count.values():
            if i >=2:
                res = True
                break
        
        return res
obj = Solution()
print(obj.hasDuplicate([1,2,3,3]))