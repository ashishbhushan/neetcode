class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i,j = 0,n-1
        while i<j:
            numsum = numbers[i]+numbers[j]
            if numsum < target:
                i+=1
            elif numsum > target:
                j-=1
            else:
                if i!=j:
                    return [i+1,j+1]