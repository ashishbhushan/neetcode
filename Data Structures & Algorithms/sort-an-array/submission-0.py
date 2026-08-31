class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left, right):
            result = []
            i,j,n,m = 0,0,len(left),len(right)

            while i<n and j<m:
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
                
            if i<n:
                while i<n:
                    result.append(left[i])
                    i += 1
            if j<m:
                while j<m:
                    result.append(right[j])
                    j += 1
            
            return result
            

        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            
            mid = len(arr)//2
            leftHalf = arr[:mid]
            rightHalf = arr[mid:]

            sortedLeft = mergeSort(leftHalf)
            sortedRight = mergeSort(rightHalf)
        
            return merge(sortedLeft, sortedRight)

        return mergeSort(nums)
