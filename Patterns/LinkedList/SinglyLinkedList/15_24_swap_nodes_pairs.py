"""
Leetcode 24: Swap Nodes in Pairs

Question:
Given a linked list, swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
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

    def swapPairs(self, head):
        """
        Approach:
        2 pointer approach:
        - prev, current
        - swap the nodes
        - move the pointers
        - return the dummy node's next node
        """
        # init pointers
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head

        # traverse the list
        while current and current.next:

            nextNode = current.next
            current.next = nextNode.next
            prev.next = nextNode
            nextNode.next = current

            prev = current
            current = current.next
        
        return dummy.next


if __name__ == "__main__":
    # create a linked list: 1 -> 2 -> 3 -> 4
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    print("Original list:")
    head.printList(head)
    print("List after swapping pairs:")
    res = head.swapPairs(head)
    head.printList(res)