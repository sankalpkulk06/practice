"""
Leetcode 328: Odd Even Linked List

Question:
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
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

    def oddEvenList(self, head):
        """
        Approach:
        - create two pointers: odd and even
        - odd pointer will point to the odd nodes
        - even pointer will point to the even nodes
        - traverse the list and add the odd nodes to the odd pointer and the even nodes to the even pointer
        - return the head of the odd nodes
        """
        # init pointers
        odd = head
        even = head.next
        even_head = even

        # traverse the list
        while even and even.next:
            # add the odd nodes to the odd pointer
            odd.next = even.next
            odd = odd.next

            # add the even nodes to the even pointer
            even.next = odd.next
            even = even.next

        # connect the odd nodes to the even nodes
        odd.next = even_head
        return head

    def main(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        self.oddEvenList(head)
        self.printList(head)
        return head

if __name__ == "__main__":
    obj = ListNode()
    obj.main()