class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0
        count = {}
        ans = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            if (r-l+1)-maxf <= k:
                ans = max(ans, r-l+1)
            else:
                count[s[l]] -= 1
                l+=1
        return ans