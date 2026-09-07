# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        traverse=head
        elements=[]
        ans=head
        ret=head

        while traverse!=None:
            elements.append(traverse.val)
            traverse=traverse.next
    
        for i in range(len(elements)-1,-1,-1):
            ans.val=elements[i]
            ans=ans.next
        
        return head





        