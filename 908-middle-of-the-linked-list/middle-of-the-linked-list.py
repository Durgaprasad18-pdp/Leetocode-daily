# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        len = 0
        while(head!=None):
            len = len +1
            head = head.next
        head = temp
        mid = (len//2)+1
        count = 0
        while(head!=None):
            count = count +1
            if count==mid:
                return head
            head = head.next
                      

        