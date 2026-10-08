class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we need to return the array that shows the top k amount frequencies in a string
        #i.e k=3 is asking, what are the top 3 elements that appear in the top-3 frequncies

        #we need to count
            #each unique num
            #it's frequency
            #keep track of the elements that have count >k

        freq = {}

        for num in nums: #for each number in the ray, append it to the set, if it doesn't exist
            freq[num] = freq.get(num, 0)+1 #if it does exist add 1

        #sort? 
        nums_sorted = sorted(freq, key=lambda num: freq[num], reverse=True)
        return nums_sorted[:k]

