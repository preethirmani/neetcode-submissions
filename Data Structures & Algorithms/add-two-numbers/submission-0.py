# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        c2 = l2
        result = ListNode()
        current = result
        carry = 0
        while c1 or c2 or carry > 0:
            temp_sum = (c1.val if c1 else 0)+ (c2.val if c2 else 0) + carry
            carry = temp_sum//10
            current.next = ListNode(temp_sum % 10)
            current = current.next
            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next
        
        return result.next