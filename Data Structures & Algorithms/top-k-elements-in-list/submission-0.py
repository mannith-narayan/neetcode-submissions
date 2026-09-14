class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = defaultdict(int)
        for x in nums:
            dict1[x] +=1
        
        sorted_dict1 = dict(sorted(dict1.items(), key=lambda item: item[1], reverse = True))
        return list(sorted_dict1.keys())[:k] 