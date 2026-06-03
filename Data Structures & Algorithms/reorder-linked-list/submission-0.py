# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow  = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next= None
        #Reverse 2nd list

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        #merging 2 lists

        first = head
        last =  prev
        
        while last:
            temp1 = first.next
            temp2 = last.next
            first.next = last
            last.next = temp1
            first = temp1
            last = temp2
        
        
