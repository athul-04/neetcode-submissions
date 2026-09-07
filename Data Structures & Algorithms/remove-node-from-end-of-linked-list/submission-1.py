# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size=0
        sizeptr=head
        while sizeptr:
            size+=1
            sizeptr=sizeptr.next
        print(size)
        removeIndex=size-n

        i=0
        traverse=head
        if removeIndex==0: return head.next
        for i in range(0,removeIndex-1):traverse=traverse.next
        if traverse.next==None or traverse.next.next==None: 
            traverse.next=None
            return head
        traverse.next=traverse.next.next
        return head

        