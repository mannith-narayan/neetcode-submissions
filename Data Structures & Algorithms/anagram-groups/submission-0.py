class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_dict = defaultdict(list)
        for x in strs:
            arr = [0]*26
            for c in x:
                arr[ord(c) - ord("a")] += 1
            a_dict[tuple(arr)].append(x)
        return list(a_dict.values())
