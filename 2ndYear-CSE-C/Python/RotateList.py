# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # 1. Calculate the length and find the actual tail
        last_node = head
        length = 1
        while last_node.next:
            last_node = last_node.next
            length += 1
            
        # 2. Adjust k (if k > length, we only need the remainder)
        k = k % length
        if k == 0:
            return head
            
        # 3. Connect the tail to the head to make it circular
        last_node.next = head
        
        # 4. Find the new tail: it's at position (length - k - 1)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
            
        # 5. Set the new head and break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
