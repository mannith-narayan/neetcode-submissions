class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = defaultdict(int)
        for x in nums:
            dict1[x] +=1
        
        # sorted_dict1 = dict(sorted(dict1.items(), key=lambda item: item[1], reverse = True))
        # return list(sorted_dict1.keys())[:k] 

        # bucket sort

        bucket_array = [[] for i in range(len(nums)+1)]
        for num, count in dict1.items():
            bucket_array[count].append(num)

        result = []
        for i in range(0, len(bucket_array)):
            for num in bucket_array[i]:
                result.append(num)
        
        return result[-k:]
