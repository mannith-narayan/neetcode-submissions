class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_1 = ""
        s = s.lower()
        
        for a in s:
            if (a.isalnum()):
                s_1 += str(a)
            else:
                continue
        
        s_2 = s_1[::-1]
        
        return (s_1 == s_2)
        