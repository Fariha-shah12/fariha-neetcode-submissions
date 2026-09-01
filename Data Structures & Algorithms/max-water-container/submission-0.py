class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        l,r= 0, len(heights)-1
        while l <r:
            w = r-l
            h = min(heights[l], heights[r])
            area = w * h
            maxarea = max(area, maxarea)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxarea
        