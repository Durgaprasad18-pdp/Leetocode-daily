# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        ans = []
        while(head!=None):
            ans.append(head.val)
            head = head.next
        head = l
        for i in range(0,len(ans),2):
            head.val = ans[i]
            head = head.next
        for i in range(1,len(ans),2):
            head.val = ans[i]
            head = head.next
        head = l
        return head            
        