from LinkedList import Node


class DoublyEndedList:
    def __init__(self,head,tail):
        self.head = Node(head.val)
        self.tail = Node(tail.val)
        self.head.next = self.tail

    def insert(self,val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        if self.tail is not None:
            self.tail.next= newNode
            self.tail = newNode

    def display(self):
        current = self.head
        while current.next is not None:
            print(current.val)
            current = current.next
        print(self.tail.val)


head = Node(1)
tail = Node(2)
l = DoublyEndedList(head,tail)
l.insert(3)
l.insert(4)

l.display()
