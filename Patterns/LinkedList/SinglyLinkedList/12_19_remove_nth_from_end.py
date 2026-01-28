"""
Leetcode 19: Remove Nth Node From End of List

Question:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
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
    
    def printNode(self, head):
        print("Node value: ", head.val)

    def removeNthFromEnd(self, head, n):
        """
        2 Pointer Approach:
        - L and R
        - we want the difference between the nodes to be "n" nodes
        - now traverse till R is at the end of the list
        - this will make sure that L is at the node we want to delete
        
        need:
        - L, R
        - dummy node
        """

        # init pointers
        dummy = ListNode(0)
        dummy.next = head
        L = dummy
        R = head

        # mode R to n nodes ahead of L
        while n > 0 and R:
            R = R.next
            n -= 1
        # R is now n nodes ahead of L

        # traverse till R is at the end of the list
        while R.next:
            L = L.next
            R = R.next
        
        # L is now at the node we want to delete
        L.next = L.next.next

        return dummy.next

if __name__ == "__main__":
    # create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print("Original list:")
    head.printList(head)
    print("List after removing nth node from end:")
    res = head.removeNthFromEnd(head, 2)
    head.printList(res)