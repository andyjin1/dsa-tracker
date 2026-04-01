# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        slow = dummy
        fast = head 
        dummy.next = head

        while fast:
            for _ in range(k):
                if not fast:
                    return dummy.next
                fast = fast.next 
            
            curr_group_tail = slow.next

            # reverse logic
            prev = None
            curr = slow.next
            
            while curr != fast:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp 
            
            slow.next = prev
            curr_group_tail.next = curr
            slow = curr_group_tail

        return dummy.next
