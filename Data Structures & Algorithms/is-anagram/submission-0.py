class Solution:
    
    def convert_to_dict(self, s:str) -> dict:
        word_dict = {}
        for x in range(len(s)):
            if s[x] in word_dict:
                word_dict[s[x]] += 1
            else:
                word_dict[s[x]] = 1
        return word_dict

    def isAnagram(self, s: str, t: str) -> bool:
        s_1 = self.convert_to_dict(s)
        t_1 = self.convert_to_dict(t)
        print(s_1, t_1)
        return s_1 == t_1


