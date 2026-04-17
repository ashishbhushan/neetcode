class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2
        if len(a)>len(b):
            a,b = b,a
        
        m = len(a)
        n = len(b)
        half = (m+n+1)//2
        low, high = 0,m

        while low<=high:
            i = (low+high)//2
            j = half - i
            leftA = a[i-1] if i>0 else float("-inf")
            rightA = a[i] if i<m else float("inf")
            leftB = b[j-1] if j>0 else float("-inf")
            rightB = b[j] if j<n else float("inf")

            if leftA<=rightB and leftB<=rightA:
                if (m+n)%2 == 0:
                    return (max(leftA,leftB)+min(rightA,rightB))/2
                else:
                    return max(leftA,leftB)
            elif leftA>rightB:
                high = i-1
            else:
                low = i+1