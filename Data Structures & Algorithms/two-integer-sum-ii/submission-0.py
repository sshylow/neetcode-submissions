class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1

        while left < right: 
            total = numbers[left] + numbers[right] #what is our current total at this L and R?

            if total == target:
                return [left+1,right+1] #1-indexed nums so we add 1

            elif total < target: #if total is greater, that means we need to move the left index up more!
                left += 1
            else: 
                right -=1 #if it's less we go down from the right bc the right most num is too big
    