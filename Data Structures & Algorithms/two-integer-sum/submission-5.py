class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums):
            indices[n] = i

        for i, val in enumerate(nums):
            rem = target - val
            if rem in indices and indices[rem] != i:
                if indices[rem]<i:
                    return [indices[rem],i]
                else:
                    return [i,indices[rem]]
        
        return []