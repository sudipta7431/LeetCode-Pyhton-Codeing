class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new = current = ListNode()
        carry = 0
        while(l1 or l2):
            if l1 and l2:
                summ = carry + l1.val + l2.val
                current.next = ListNode(summ % 10)
                carry = summ // 10
                current = current.next
            elif l1:
                summ = carry + l1.val
                current.next = ListNode(summ % 10)
                carry = summ // 10
                current = current.next                
            elif l2:
                summ = carry + l2.val
                current.next = ListNode(summ % 10)
                carry = summ // 10
                current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next   
        if carry > 0:
            current.next = ListNode(carry)    
        
        
        return new.next