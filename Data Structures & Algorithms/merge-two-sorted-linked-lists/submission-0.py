# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #temp1 = list1
        # temp2 = list2
        # while temp1 != None and temp2 != None:
        #     if temp1.val <= temp2.val:
        #         newtemp1 = temp1.next
        #         temp1.next = temp2
        #         newtemp2 = temp2.next
        #         temp2.next = newtemp1
        #     else:

        temp1 = []
        while list1 != None:
            temp1.append(list1.val)
            list1 = list1.next

        while list2 != None:
            temp1.append(list2.val)
            list2 = list2.next

        temp1.sort()
        length = len(temp1)
        dummy = ListNode(0)
        newtemp = dummy
        for i in range(length):
           newhead =  ListNode(temp1[i])
           dummy.next = newhead
           dummy = newhead

        return newtemp.next


        




        


