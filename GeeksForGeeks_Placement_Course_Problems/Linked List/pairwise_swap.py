class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def pairwise_swap(head):
    temp = head
    while temp != None and temp.next!=None:
        temp.data, temp.next.data = temp.next.data, temp.data
        temp = temp.next.next
    
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
head = pairwise_swap(head)
print()
printLinkedList(head)