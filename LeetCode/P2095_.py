# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return None
        
        MidNode = head
        EndNode = head
        prevNode = None
        while EndNode.next:
            EndNode = EndNode.next
            prevNode = MidNode
            MidNode = MidNode.next
            if EndNode.next: # 2칸가기
                EndNode = EndNode.next
            
        prevNode.next = MidNode.next # delete
        MidNode = None

        return head