# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        
        cnt = 3
        ret = head
        odd_prev= head
        even_prev = head.next
        even_head = head.next 
        head = head.next.next

        while head:
            if cnt % 2 == 1:
                odd_prev.next = head
                odd_prev = odd_prev.next
            else:
                even_prev.next = head
                even_prev = even_prev.next
            head = head.next
            cnt += 1

        odd_prev.next = even_head
        even_prev.next = None

        return ret

# Better Solution
# class Solution:
#     def oddEvenList(self, head: ListNode | None) -> ListNode | None:
#         if not head or not head.next:
#             return head

#         odd = head
#         even = head.next
#         even_head = even

#         while even and even.next:
#             odd.next = even.next
#             odd = odd.next

#             even.next = odd.next
#             even = even.next

#         odd.next = even_head

#         return head