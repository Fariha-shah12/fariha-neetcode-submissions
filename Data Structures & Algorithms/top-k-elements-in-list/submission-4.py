from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)  
        bucket = [0] * (len(nums)+1)    #[0,0,0,0,0,0...0]
        #count = {[1:1, 2:2,3:3]}
        for  num,freq in count.items():
            if bucket[freq] ==0:
                bucket[freq] = [num]
            else:
                bucket[freq].append(num)
            #bucket=[0,1,2,3...0]
            #k=2
        newlst =[]
        for i in range(len(nums), -1, -1):
            if bucket[i] !=0:
                newlst.extend(bucket[i])
            if k == len(newlst):
                break
        return newlst

