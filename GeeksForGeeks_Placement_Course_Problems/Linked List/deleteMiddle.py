def lengthLinkedList(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def deleteMid(head):
    length = lengthLinkedList(head)
    if length == 1:
        return head
    if length == 2:
        head.next = None
        return head
    mid = length // 2
    current = head
    for i in range(mid-1):
        current = current.next
    current.next = current.next.next
    return head