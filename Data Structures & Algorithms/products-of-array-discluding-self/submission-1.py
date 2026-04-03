class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # output = [1]*n
        # pre = []
        # suff = []
        # preprod, sufprod = 1,1
        # for i in nums:
        #     preprod *= i
        #     pre.append(preprod)
        # for j in reversed(nums):
        #     sufprod *= j
        #     suff.append(sufprod)
        # suff.reverse()
        # for i in range(n):
        #     if i==0:
        #         output[i] = suff[i+1]
        #     elif i==len(nums)-1:
        #         output[i] = pre[i-1]
        #     else:
        #         output[i] = pre[i-1]*suff[i+1]
        # return output

        n = len(nums)
        output = [1]*n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1,-1,-1):
            output[i] *= suffix
            suffix *= nums[i]

        return output