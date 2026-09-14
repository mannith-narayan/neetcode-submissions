class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for x in strs:
            length = len(x)
            encoded_string += str(length) + "$" + x

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
                
            length = int(s[i:j])
            
            string_start = j + 1
            string_end = string_start + length
            decoded_strings.append(s[string_start:string_end])
            
            i = string_end

        return decoded_strings
