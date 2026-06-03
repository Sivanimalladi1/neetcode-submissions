# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def kthNode(self,temp,k):
        k-=1
        while(temp!=None and k>0):
            k-=1
            temp = temp.next
        return temp

    def reverse(self, temp):
        if temp is None or temp.next is None:
            return head
        newhead = self.reverse(temp.next)
        front = temp.next
        front.next = temp
        temp.next = None
        return newhead

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        kthnode = None
        nextNode = None
        prevnode = None
        while(temp!=None):
            knode = self.kthNode(temp,k)
            if(knode==None):
                if(prevNode):
                    prevNode.next = temp
                break
            nextNode = knode.next
            knode.next = None
            self.reverse(temp)
            if(head==temp):
                head = knode
            else:
                prevNode.next = knode

            prevNode = temp
            temp = nextNode
        return head

            
