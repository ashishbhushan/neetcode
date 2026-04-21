class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        
        l = 0
        s_count = {}
        minstr = ""
        have, need = 0,len(t_count)

        for r in range(len(s)):
            s_count[s[r]] = s_count.get(s[r], 0) + 1

            if s[r] in t_count and s_count[s[r]] == t_count[s[r]]:
                have+=1
        
            while have == need:
                if minstr == "" or (r-l+1) < len(minstr):
                    minstr = s[l:r+1]
                if s[l] in t_count:
                    s_count[s[l]] -= 1
                    if s_count[s[l]] < t_count[s[l]]:
                        have -= 1
                l+=1

        return minstr