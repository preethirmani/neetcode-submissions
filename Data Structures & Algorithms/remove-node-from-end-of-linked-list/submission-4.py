# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        count = 0
        while current:
            count += 1
            current = current.next
        k = count - n
        if k == 0:
            head = head.next
        else:
            i = 0
            current = head
            while i < k - 1:
                current = current.next
                i += 1
            current.next = current.next.next
        return head

        