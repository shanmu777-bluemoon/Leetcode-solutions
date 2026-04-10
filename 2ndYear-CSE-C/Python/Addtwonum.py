# REMOVE OR COMMENT OUT THE LISTNODE DEFINITION BELOW:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        
        while l1:
            s1.append(l1.val)
            l1 = l1.next
            
        while l2:
            s2.append(l2.val) # Changed from s2.val to l2.val
            l2 = l2.next
            
        ans = None
        carry = 0
        
        while s1 or s2 or carry:
            a = s1.pop() if s1 else 0
            b = s2.pop() if s2 else 0
            
            total = a + b + carry
            carry = total // 10
            
            node = ListNode(total % 10)
            node.next = ans
            ans = node
            
        return ans
