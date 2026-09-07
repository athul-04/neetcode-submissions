# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1==None: return list2
        if list2==None: return list1

        if list1.val<=list2.val:
            curr=ListNode(list1.val)
            list1=list1.next
        else:
           curr=ListNode(list2.val)
           list2=list2.next 
        ans=curr
        
        while list1!=None and list2!=None:

            if list1.val<=list2.val:
                temp=ListNode(list1.val)
                list1=list1.next
            else:
                temp=ListNode(list2.val)
                list2=list2.next
            curr.next=temp
            curr=curr.next

        
        while list1!=None:
            curr.next=ListNode(list1.val)
            list1=list1.next
            curr=curr.next
        while list2!=None:
            curr.next=ListNode(list2.val)
            list2=list2.next
            curr=curr.next
        

        return ans
        