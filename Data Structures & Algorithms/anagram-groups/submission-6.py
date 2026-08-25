class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqdict = {}

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            key = tuple(count)
            if key in freqdict:
                freqdict[key].append(word)
            else:
                freqdict[key] = [word]
            
        return list(freqdict.values())