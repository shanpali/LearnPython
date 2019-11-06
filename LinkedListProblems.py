class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#leedcode problem for adding 2 linked list
class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        fake = ListNode(0)
        p = fake
        p1 = l1
        p2 = l2
        carry = 0
        while p1 is not None or p2 is not None:
            sum = carry
            if p1 is not None:
                sum = sum + p1.val
                p1 = p1.next
            if p2 is not None:
                sum = sum + p2.val
                p1 = p2.next
            if sum > 9:
                carry = 1
                sum = sum - 10
            else:
                carry = 0
            l = ListNode(sum)
            p.next = l
            p = p.next
        if carry > 0:
            l = ListNode(carry)
            p.next = l
        return fake.next

    def print_list(self,l:ListNode)->ListNode:
        s=None
        while l is not None:
            s="-->"+str(l.val)
            l=l.next
        print(s)




l1=ListNode(2)
l1.next=ListNode(4)
l1.next.next=ListNode(3)
l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(4)

s=Solution()
added=s.add_two_numbers(l1,l2)
#todo issue with print. its takes more time.need to resolve
s.print_list(added)



