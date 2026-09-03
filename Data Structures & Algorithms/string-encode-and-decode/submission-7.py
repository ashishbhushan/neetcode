class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i))+"#"+i
        return res

    def decode(self, s: str) -> List[str]:
        result = []
        i,j = 0,0
        while i < len(s):
            if s[i] == "#":
                length = int(s[j:i])
                result.append(s[i+1:min(len(s),i+1+length)])
                j = i+1+length
                i = i+1+length
            i+=1
        return result
