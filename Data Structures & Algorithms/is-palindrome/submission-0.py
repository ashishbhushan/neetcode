class Solution:
    def isPalindrome(self, s: str) -> bool:
        # newstr = "".join(x for x in s if x.isalnum())
        # newstr = "".join(filter(str.isalnum, s))
        n = len(s)
        i,j = 0,n-1
        while i<j:
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            else:
                if not s[i].lower() == s[j].lower():
                    return False
                i+=1
                j-=1
        return True
            
        