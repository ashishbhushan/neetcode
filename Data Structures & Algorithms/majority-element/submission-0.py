class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqdict = {}
        n = len(nums)//2
        for num in nums:
            freqdict[num] = freqdict.get(num, 0) + 1
        
        return next(key for key, value in freqdict.items() if value > n)