class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bucket = set()
        left = 0 
        longest = 0

        for right in range(len(s)):
            while s[right] in bucket: #is the character in the bucket? 
                bucket.remove(s[left])
                left +=1
            #char not in bucket
            bucket.add(s[right])
            longest = max(longest, right-left+1)

        return longest
