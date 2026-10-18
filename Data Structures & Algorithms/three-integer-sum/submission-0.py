class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sorting for better nav on pointers
        nums = sorted(nums)
        res = [] 
        
        for i in range(len(nums)-2): #we'll skip the repeated vals

            if i > 0 and nums[i] == nums[i-1]:
                continue




            left = i+1
            right = len(nums)-1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
    
                #if it's less, we need less negaitves (?) move left up 1
                if total < 0:
                    left +=1
                #more? too many positives move right down 1
                elif total > 0:
                    right -=1
                else: 
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # skip repeated values so we don't add duplicate triplets
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res