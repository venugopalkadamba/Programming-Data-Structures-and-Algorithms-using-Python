# LINKED LIST IMPLEMENTATION

# Node Class

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None
    
    # inserts data at beginning of the linked list
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    # inserts data at the end of the linked list
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
    
    # deletes the previus linked list and creates a new linked list with the input data
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    # inserts data at specified index
    def insert_at(self, index, data):
        if index<0 or index>self.length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        i = 0
        temp = self.head
        while temp:
            if i == index-1:
                temp.next = Node(data,temp.next)
                break
            temp = temp.next
            i+=1

    # inserts a value after the first occurance of a particular data
    def insert_after_value(self, after_data, data_to_insert):
        temp = self.head
        while temp:
            if temp.data == after_data:
                temp.next = Node(data_to_insert, temp.next)
                break
            temp = temp.next


    # removes the element at the specified index
    def remove_at(self, index):
        if index<0 or index>=self.length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return
        
        i = 0
        temp = self.head
        while temp:
            if i == index-1:
                temp.next = temp.next.next
                break
            temp = temp.next
            i+=1

    # returns the length of the linked list   
    def length(self):
        c = 0
        temp = self.head
        while temp:
            c+=1
            temp = temp.next
        return c
    
    # prints the data in the linked list
    def print(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end = " ")
                temp = temp.next
            print()

def mergeList(head1, head2):
    temp1 = head1
    temp2 = head2
    l1 = []
    l2 = []
    while temp1!=None and temp2!=None:
        l1.append(temp1.data)
        l2.append(temp2.data)
        temp1 = temp1.next
        temp2 = temp2.next
    l = sorted(l1+l2)
    head = Node(l[0], None)
    for i in l[1:]:
        temp = head
        while temp.next!=None:
            temp = temp.next
        temp.next = Node(i)
    temp = head
    s = ''
    while temp!=None:
        s = s+str(temp.data)+'->'
        temp = temp.next
    print(s[:-2])

l1 = LinkedList()
l1.insert_values([1,2,3,4])
l2 = LinkedList()
l2.insert_values([1,3,5,7])

mergeList(l1.head, l2.head)