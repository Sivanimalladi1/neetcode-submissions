# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        
        if count == n: #remove head
            newhead = head.next
            return newhead
        
        temp = head
        nnode = count - n
        count = nnode
        if nnode == 0: #only 1 node, 1 mode to remove
            return None
        while count  != 1: #middle node remove
            temp = temp.next
            count -= 1

        print("val", temp.val)
        
        temp.next = temp.next.next
        
        return head


        
            


