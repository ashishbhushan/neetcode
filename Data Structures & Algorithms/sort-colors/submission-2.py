class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = {0:0, 1:0, 2:0}
        for num in nums:
            freq[num] = freq.get(num) + 1
        
        s = 0
        for i in range(3):
            times = freq[i]
            for j in range(times):
                nums[s] = i
                s+=1
        