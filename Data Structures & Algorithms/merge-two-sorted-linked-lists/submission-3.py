# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        result = ListNode()
        new_node = result
        while current1 and current2:
            
            if current1 and current1.val < current2.val:
                new_node.next = current1
                current1 = current1.next
            else:
                new_node.next = current2
                current2 = current2.next
            new_node = new_node.next
        if current1:
            new_node.next = current1
        else:
            new_node.next = current2
        return result.next


