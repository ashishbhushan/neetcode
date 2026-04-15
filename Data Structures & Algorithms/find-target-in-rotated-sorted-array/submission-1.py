class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(left, right, target):

            # print(left, right)
            if left > right : return -1
            mid = (left + right) // 2

            if nums[mid] == target: return mid
            if nums[left] == target : return left
            if nums[right] == target: return right

            if right == left : return -1
            
            # in the rotated part
            if nums[mid] > nums[right]:
                if target > nums[mid] :
                    left = mid + 1
                    return binary_search(left, right, target)
                if target < nums[mid] :
                    if target < nums[right]:
                        left = mid + 1
                        return binary_search(left, right, target)
                    else :
                        right = mid - 1
                        return binary_search(left, right, target)
            
            # in normal part
            if nums[mid] < nums[right] :
                if target < nums[mid] :
                    right = mid - 1
                    return binary_search(left, right, target)
                if target > nums[mid] :
                    if target > nums[right] :
                        right = mid - 1
                        return binary_search(left, right, target)
                    else :
                        left = mid + 1
                        return binary_search(left, right, target)
            
        return binary_search(0, len(nums)-1, target)
        return -1