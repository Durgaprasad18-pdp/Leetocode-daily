# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        temp = head
        while(head!=None):
            a.append(head.val)
            head = head.next
        a.sort()
        head = temp
        i = 0
        while(head!=None):
            head.val = a[i]
            i= i+1
            head = head.next
        head = temp
        return head         
        