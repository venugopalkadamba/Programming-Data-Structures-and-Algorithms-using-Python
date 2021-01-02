def lengthLinkedList(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count
    

def intersetPoint(head1,head2):
    len1 = lengthLinkedList(head1)
    len2 = lengthLinkedList(head2)
    
    visited = {}
    if len1 < len2:
        while head1:
            visited[head1] = True
            head1 = head1.next
        while head2:
            try:
                if visited[head2]:
                    return head2.data
            except:
                head2 = head2.next
    else:
        while head2:
            visited[head2] = True
            head2 = head2.next
        while head1:
            try:
                if visited[head1]:
                    return head1.data
            except:
                head1 = head1.next
    return -1