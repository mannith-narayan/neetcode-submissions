class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        count = 0
        index = []
        for i in range(len(nums)):
            if nums[i]!=0:
                product = product*nums[i]
            if nums[i] == 0:
                count+=1
                index.append(i)
        
        result = []

        if (count > 1):
            return [0]*len(nums)

        if (count == 1):
            for i in range(len(nums)):
                if i in index:
                    result.append(product)
                else:
                    result.append(0)

        else:
            for i in range(len(nums)):
                result.append(int(product/nums[i]))

        return result