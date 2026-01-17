"""
Leetcode 203: Remove Linked List Elements

Question:
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
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
    
    def removeElements(self, head, val):
        """
        Approach:
        - create a dummy node to store the new list
        - use two pointers: prev and curr
        - if the current node's value is equal to val, skip the node
        - if the current node's value is not equal to val, add the node to the new list
        - return the dummy node's next node
        """
        # init pointers
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        # traverse
        while curr:
            # if node is encountered with val
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return dummy.next
    
if __name__ == "__main__":
    # create a linked list: 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)
    print("Original list:")
    head.printList(head)
    print("List after removing elements:")
    head.removeElements(head, 6)
    head.printList(head)