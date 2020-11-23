class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLinkedList(head):
    prev, nxt = None, None
    current = head

    while current != None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    head = prev
    return head

def addLists(first, second):
    first = reverseLinkedList(first)
    second = reverseLinkedList(second)
    
    carry = 0
    new_list = None
    new_head = None
    
    f1 = first
    f2 = second
    
    while f1!=None or f2!=None or carry:
        t1 = 0 if f1 is None else f1.data
        t2 = 0 if f2 is None else f2.data
        Sum = carry + t1 + t2
        num = Sum
        if Sum >= 10:
            num = Sum - 10
            carry = 1
        else:
            carry = 0
        
        if new_list is None:
            new_list = Node(num)
            new_head = new_list
        else:
            new_list.next = Node(num)
            new_list = new_list.next
        
        if f1 is not None:
            f1 = f1.next
        if f2 is not None:
            f2 = f2.next
    
    return reverseLinkedList(new_head)