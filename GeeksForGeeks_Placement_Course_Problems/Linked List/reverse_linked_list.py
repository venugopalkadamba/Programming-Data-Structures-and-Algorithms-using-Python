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

def printLinkedList(head):
    temp = head
    while temp!=None:
        print(temp.data, end=" ")
        temp = temp.next


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

head = n1

printLinkedList(head)
head = reverseLinkedList(head)
print()
printLinkedList(head)