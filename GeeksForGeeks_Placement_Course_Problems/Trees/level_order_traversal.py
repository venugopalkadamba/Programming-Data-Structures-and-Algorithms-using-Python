class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder(head):

    if head != None:
        inorder(head.left)
        print(head.value, end=" ")
        inorder(head.right)
    else:
        return
    
def level_order_traversal(head):
    queue = []
    queue.append(head)
    while len(queue) != 0:
        if queue[0] is not None:
            queue.append(queue[0].left)
            queue.append(queue[0].right)
            print(queue[0].value, end=" ")
        del queue[0]



head = Node(10)
head.left = Node(20)
head.right = Node(30)

head.left.left = Node(40)
head.left.right = Node(50)

head.left.right.left = Node(70)
head.left.right.right = Node(80)

head.right.right = Node(60)

level_order_traversal(head)