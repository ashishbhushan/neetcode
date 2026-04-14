import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i,j = 1,max(piles)
        ans = 0
        while i<=j:
            k = (i+j)//2
            hours = sum([math.ceil(x/k) for x in piles])
            if hours<=h:
                ans = k
                j = k-1
            else:
                i = k+1

        return ans