# IMPLEMENTATION OF DOUBLY LINKED LIST

class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedlIst:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            self.head.prev = node
            node.next = self.head
            self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            node = Node(data)
            temp.next = node
            node.prev = temp

    def insert_at(self, index, data):
        if index<0 or index>self.length():
            raise Exception("Enter a valid index")

        if index == 0:
            self.insert_at_beginning(data)
        else:
            temp = self.head
            c = 0
            while temp:
                if c == index-1:
                    node = Node(data)
                    node.prev = temp
                    node.next = temp.next
                    temp.next = node
                    break
                temp = temp.next
                c+=1
    
    def delete_at(self, index):
        if index<0 or index >= self.length():
            raise Exception("Enter a Valid Index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        
        if index == self.length()-1:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None
        else:
            temp = self.head
            c = 0
            while temp:
                if c == index-1:
                    temp.next.next.prev = temp
                    temp.next = temp.next.next
                    break
                temp = temp.next
                c+=1

    def length(self):
        c = 0
        temp = self.head
        while temp:
            c+=1
            temp = temp.next
        return c
    
    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next

l = DoublyLinkedlIst()
l.insert_at_beginning(2)
l.insert_at_beginning(3)
l.insert_at_end(4)
l.insert_at_end(5)
l.print()
print()
l.delete_at(2)
l.print()