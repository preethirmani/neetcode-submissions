# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        count = 0
        i = 0
        

        while current:
            count += 1
            current = current.next
        
        node_to_remove  = count - n
        if node_to_remove == 0 :
            if count == 1:
                head = None
            else :
                head = head.next
        else:
            current = head

            while i < node_to_remove - 1:
                current = current.next
                i += 1


            current.next = current.next.next


        return head
        