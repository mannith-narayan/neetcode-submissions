class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s_1 = ""
        # s = s.lower()
        
        # for a in s:
        #     if (a.isalnum()):
        #         s_1 += str(a)
        #     else:
        #         continue
        
        # s_2 = s_1[::-1]
        
        # return (s_1 == s_2)

        s = s.lower()
        l = 0
        r = len(s)-1

        while l < r:
            if s[l] == s[r] and s[l].isalnum() and s[r].isalnum():
                l+=1
                r-=1
                continue;
            elif s[l].isalnum() == False:
                l+=1
            elif s[r].isalnum() == False:
                r-=1
            else:
                return False
        
        return True
            

        
        
        