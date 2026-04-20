class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        for s in s1:
            s1_count[s] = s1_count.get(s, 0) + 1

        print(s1_count)
        
        s2_count = {}
        l = 0
        for r in range(len(s2)):
            s2_count[s2[r]] = s2_count.get(s2[r], 0) + 1
            if s2_count == s1_count:
                return True
            if r >= len(s1)-1:
                if s2_count[s2[l]] > 1:
                    s2_count[s2[l]] -= 1
                else:
                    del s2_count[s2[l]]
                l+=1

        return False