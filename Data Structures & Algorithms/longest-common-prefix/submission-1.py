class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for string in range(1, len(strs)):
            a = strs[string]

            for x in range (0, len(prefix)):
                if x >= len(a) or prefix[x] != a[x] :
                        prefix = prefix[0:x]
                        break;
                        
                    
        return prefix

                    
            