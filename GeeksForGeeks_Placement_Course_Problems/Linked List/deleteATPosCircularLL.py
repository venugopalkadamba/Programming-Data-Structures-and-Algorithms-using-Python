def deleteAtPosition(head,pos):
    current = head
    if pos == 1:
        while current.next != head:
            current = current.next
        head = current.next.next
        current.next = head
    else:
        prev = None
        for i in range(pos-1):
            prev = current
            current = current.next
        prev.next = current.next
    return head