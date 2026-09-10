class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxcount = 0
        for num in numset:
            if num-1 not in numset:
                count = 0
                while num+count in numset:
                    count+=1
                maxcount = max(maxcount,count)
        return maxcount
            

