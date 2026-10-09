class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #[1,2,3]
        #i=0 -> 2 x 3  = nums[1] x nums[2]
        
        n = len(nums)
        res = [1] * n

        # put the product of numbers to the left of each index in res
        left_product = 1
        for i in range(n):
            res[i] = left_product
            left_product *= nums[i]

        # multiply by the product of numbers to the right of each index
        right_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]

        return res