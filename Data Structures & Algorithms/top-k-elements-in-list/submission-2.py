class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsdict = {}
        for num in nums:
            numsdict[num] = numsdict.get(num, 0) +1

        # sortedlist = sorted(numsdict.items(), key=lambda item: item[1], reverse=True)
        # return [sortedlist[i][0] for i in range(k)]

        numslist = [[] for _ in range(len(nums)+1)]
        for key,val in numsdict.items():
            numslist[val].append(key)

        result = []
        for sublist in reversed(numslist):
            if len(sublist)>0:
                for i in sublist:
                    result.append(i)
                    if len(result)==k:
                        return result