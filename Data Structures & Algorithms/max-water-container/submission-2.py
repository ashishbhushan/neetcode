class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxvolume = 0
        i,j=0,n-1
        while i<j:
            volume = (j-i)*(min(heights[i], heights[j]))
            maxvolume = max(volume, maxvolume)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1

        return maxvolume