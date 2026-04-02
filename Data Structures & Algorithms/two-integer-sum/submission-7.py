class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {}
        n = len(nums)
        for k,v in enumerate(nums):
            numdict[v] = k
        
        for i in range(n):
            num = target-nums[i]
            if num in numdict:
                if i!=numdict[num]:
                    return [i,numdict[num]]