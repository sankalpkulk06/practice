def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None
    
    pointerA = headA
    pointerB = headB

    while pointerA != pointerB:

        if pointerA:
            pointerA = pointerA.next
        else:
            pointerA = headB
        if pointerB:
            pointerB = pointerB.next
        else:
            pointerB = headA
        
    return pointerA