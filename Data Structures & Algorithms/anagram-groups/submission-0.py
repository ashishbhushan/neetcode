class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strdict = {}
        for i in strs:
            sortedstr = "".join(sorted(i))
            if sortedstr in strdict:
                strdict[sortedstr].append(i)
            else:
                strdict[sortedstr] = [i]

        result = []
        for val in strdict.values():
            result.append(val)

        return result