"""
leetcode 143: Reorder List

Question:
You are given the head of a singly linked list. 
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val # value of the node
        self.next = next # pointer to the next node
    
    # print the list
    @staticmethod
    def printList(head):
        while head is not None:
            print(head.val, end=" ")
            head = head.next # move to the next node
        print()
    
    # print the node
    @staticmethod
    def printNode(head):
        print("Node value: ", head.val)
    
    # reorder the list
    @staticmethod
    def reorderList(head):
        """
        Approach:
        Phase 1: 
            - Find middle of list (fast/slow pointers)
            - reverse second half of the list
        Phase 2: 
            - merge the lists
        """

        # Phase 1: find the middle of the list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is the middle of the list

        # Phase 2: reverse the second half of the list
        second = slow.next
        slow.next = None    # eg. 2: 3 -> NULL
        prev = None

        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        # prev is the new head of the second half of the list

        # Phase 3: merge the lists
        first = head
        second = prev

        while second:
            # store the next nodes before changing the pointers
            next_node1 = first.next
            next_node2 = second.next

            # merge the lists
            first.next = second
            second.next = next_node1

            # shift the pointers
            first = next_node1
            second = next_node2

        return head
    
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.printList(head)
    head = ListNode.reorderList(head)
    head.printList(head)