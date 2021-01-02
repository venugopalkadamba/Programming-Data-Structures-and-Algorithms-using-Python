def reverse(head, k):
    prev, nxt = None, None
    current = head
    
    count = 0

    while current != None and count < k:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
        count+=1
    if nxt != None:
        head.next = reverse(nxt, k)
    return prev