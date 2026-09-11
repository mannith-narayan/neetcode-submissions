class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for x in range(len(nums)):
            n = nums[x]
            diff = target - n
            if diff in num_to_index:
                return [num_to_index[diff], x]
            else:
                num_to_index[n] = x
