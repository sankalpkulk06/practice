"""
Leetcode 206: Reverse Linked List

Question:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def printList(self, head):
        while head is not None:
            print(head.val, end=" ")
            head = head.next
        print()

    def reverseList(self, head):
        prev = None
        current = head

        # Prev -> Current -> Next_node
        while current is not None:
            next_node = current.next
            current.next = prev # Prev <- Current -> Next_node
            prev = current # move forward
            current = next_node # move forward
        return prev # return the new head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

head.printList(head)
head = head.reverseList(head)  # Capture the new head
head.printList(head)