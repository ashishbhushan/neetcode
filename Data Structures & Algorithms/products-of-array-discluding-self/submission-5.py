class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod, zero_count = 1, 0
        # for num in nums:
        #     if num:
        #         prod *= num
        #     else:
        #         zero_count += 1
        # if zero_count > 1: return [0] * len(nums)
        
        # product = [0] * len(nums)
        # for i,val in enumerate(nums):
        #     if zero_count:
        #         product[i] = 0 if val else prod
        #     else:
        #         product[i] = prod//val

        product = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            product[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for j in range(len(nums)-1,-1,-1):
            product[j] *= postfix
            postfix *= nums[j]
        
        return product