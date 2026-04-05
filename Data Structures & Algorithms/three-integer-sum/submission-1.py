class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsSorted = sorted(nums)
        # print(numsSorted)
        # -nums[i] = nums[j] + nums[k]
        n = len(numsSorted)
        visited = set()
        triplets = set()
        for i in range(n):
            if numsSorted[i]>0:
                break
            j = i+1
            k = n-1
            if numsSorted[i] in visited:
                continue
            else:
                visited.add(numsSorted[i])
            while j<k:
                # print(numsSorted[i],numsSorted[j],numsSorted[k])
                if -numsSorted[i] == (numsSorted[j] + numsSorted[k]):
                    # print("triplet found")
                    triplets.add((numsSorted[i],numsSorted[j],numsSorted[k]))
                    j+=1
                    k-=1
                elif -numsSorted[i] < (numsSorted[j] + numsSorted[k]):
                    k-=1
                else:
                    j+=1

        return [list(triplet) for triplet in triplets]