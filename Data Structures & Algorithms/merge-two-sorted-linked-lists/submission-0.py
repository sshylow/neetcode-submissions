# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #iirc we can solve this recursivley ?
        
        #base cases
        if list1 is None:
            return list2 #the mergerd result is what's in list2
        if list2 is None:  
            return list1 #the merged result is what's in list1

        #we want to compare l1's node to l2's node. whatever is greater is what we'll continously call the function on
        if list1.val<=list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
            # if the value is <= whatever the head is of list2, we know we need to put that value next! 
            # then, we can call the function on whatever is after the node we just appended + the leftovers of list2

        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2
            #same but reverse