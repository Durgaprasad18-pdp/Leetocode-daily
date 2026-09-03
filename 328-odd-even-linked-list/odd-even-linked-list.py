# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        a = []
        while(head!=None):
            a.append(head.val)
            head = head.next
        head = temp
        
        for i in range(0,len(a),2):
            head.val = a[i]
            head = head.next
        for i in range(1,len(a),2):
            head.val = a[i]
            head = head.next    
        
        head = temp
        return head            

        