# Floyd’s Cycle-Finding Algorithm

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_cycle(head):
    slow_pointer = fast_pointer =  head
    while slow_pointer and fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            return True
    return False

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n2

head = n1

print(find_cycle(head))