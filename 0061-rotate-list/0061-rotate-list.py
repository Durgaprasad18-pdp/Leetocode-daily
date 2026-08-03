class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        ans = []
        copy = head

        while head is not None:
            ans.append(head.val)
            head = head.next

        k = k % len(ans)

        if k != 0:
            ans[:] = ans[len(ans)-k:] + ans[:len(ans)-k]

        head = copy
        for i in range(len(ans)):
            head.val = ans[i]
            head = head.next
        head = copy
        return head