# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        p = dummy
        pq = []

        if not lists:
            return None
        
        for head in lists:
            if head:
                heapq.heappush(pq, (head.val, id(head), head))
                head = head.next
        
        while pq:
            _,_,curr_node = heapq.heappop(pq)
            p.next = curr_node

            if curr_node.next:
                heapq.heappush(pq, (curr_node.next.val, id(curr_node.next), curr_node.next)) 
            p = p.next
        
        return dummy.next
            