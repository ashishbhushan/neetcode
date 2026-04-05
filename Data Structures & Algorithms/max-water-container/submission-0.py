class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxvolume = 0
        for i in range(n):
            j = n-1
            while i<j:
                volume = (j-i)*(min(heights[i], heights[j]))
                maxvolume = max(volume, maxvolume)
                j-=1
        return maxvolume