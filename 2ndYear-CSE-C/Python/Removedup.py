# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        # Create a dummy node to handle cases where the head needs to be removed
        dummy = ListNode(0, head)
        prev = dummy
        
        while head:
            # If we find a sequence of duplicates
            if head.next and head.val == head.next.val:
                # Move 'head' to the end of the duplicate sequence
                while head.next and head.val == head.next.val:
                    head = head.next
                # Link 'prev' to the node AFTER the last duplicate
                prev.next = head.next
            else:
                # No duplicate found, move 'prev' forward
                prev = prev.next
            
            # Move 'head' forward for the next iteration
            head = head.next
            
        return dummy.next
