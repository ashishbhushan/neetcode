class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val in enumerate(nums):
            rem = target - val
            try:
                rem_index = nums.index(rem, i+1)
            except:
                continue
            return [i,rem_index] 
                