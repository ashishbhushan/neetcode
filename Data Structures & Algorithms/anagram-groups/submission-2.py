class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strdict = {}

        # for i in strs:
        #     sortedstr = "".join(sorted(i))
        #     if sortedstr in strdict:
        #         strdict[sortedstr].append(i)
        #     else:
        #         strdict[sortedstr] = [i]

        # return list(strdict.values())

        for str in strs:
            count = [0]*26
            for c in str:
                count[ord(c)-97] +=1
            key = tuple(count)

            if key not in strdict:
                strdict[key] = []
            strdict[key].append(str)
        
        return list(strdict.values())