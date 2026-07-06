# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = []
        while (head!=None):
            ans.append(head.val)
            head = head.next
        maxi = 0
        n = len(ans)
        for i in range(n//2):
            maxi = max(maxi,ans[i]+ans[n-1-i])
        return maxi        
        