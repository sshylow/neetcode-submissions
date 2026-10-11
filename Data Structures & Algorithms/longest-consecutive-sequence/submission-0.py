class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) #putting it as a set allows for fast look ups
        longest = 0 #counter for the longest set of nums

        for num in num_set:

            if num-1 not in num_set: #defines the new beginning per sequence
                current = num
                length = 1

                while current + 1 in num_set: #keep this loop going if there's one bigger than the current num
                    current +=1
                    length +=1

                longest=max(longest, length)

        return(longest)