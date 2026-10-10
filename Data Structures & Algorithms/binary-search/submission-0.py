class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #inution iirc 
        #split array in half
        #is the target <, >, = than the half index? 
            #< -- split the left array and continue
            #> -- split the right array and continue
            #= -- target found! return index

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right=mid-1
            else:
                left=mid+1

        return -1
        