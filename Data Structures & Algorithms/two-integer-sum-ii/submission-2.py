class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if numbers is None:
            return []

        i,j = 0,len(numbers)-1

        while i<j:
            numsum = numbers[i]+numbers[j]
            if numsum == target:
                return [i+1,j+1]
            elif numsum > target:
                j-=1
            else:
                i+=1
        
        return []