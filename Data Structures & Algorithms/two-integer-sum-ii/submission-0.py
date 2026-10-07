class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if len(numbers)==0:
            return [0,0]

        l = 0
        r = len(numbers)-1

        while l < r:
            number = numbers[l] + numbers[r]
            if number == target:
                break;
            elif number < target:
                l+=1
            elif number > target:
                r-=1

        return [l+1,r+1]

        