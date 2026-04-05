class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxpre = [0]*n
        maxsuf = [0]*n
        minheight = []
        maxvol = 0
        maxpreval, maxsufval = 0,0
        j = n-1
        for i in range(n):
            maxpre[i] = maxpreval
            maxpreval = max(height[i],maxpreval)

            maxsuf[j] = maxsufval
            maxsufval = max(height[j],maxsufval)
            j-=1
        minheight = [min(maxpre[x],maxsuf[x]) for x in range(n)]
        
        # print(height)
        # print(minheight)
        
        for i in range(n):
            vol = minheight[i] - height[i]
            if vol >0:
                maxvol+=vol
        # print(maxvol)
        return maxvol