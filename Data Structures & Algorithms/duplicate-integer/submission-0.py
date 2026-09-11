class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_count = {}
        for x in range(len(nums)):
            num = nums[x]
            if num not in nums_count:
                nums_count[num] = 1
            else:
                return True
        return False
                