class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1

        vol=0

        while i<j:
            v=min(heights[i],heights[j])*(j-i)
            vol=max(vol,v)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return vol