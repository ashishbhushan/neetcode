class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        if not nums:
            return 0
        count, maxcount = 1,1
        for num in numset:
            if num-1 not in numset:
                elm = num
                while elm+1 in numset:
                    count+=1
                    elm+=1
                maxcount = max(maxcount,count)
                count=1
        return maxcount
            

