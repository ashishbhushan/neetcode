class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()
        for i in set(s):
            s_dict[i] = s.count(i)
        for i in set(t):
            t_dict[i] = t.count(i)
        if s_dict == t_dict:
            return True
        else:
            return False