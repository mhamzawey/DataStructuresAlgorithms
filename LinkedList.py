class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = Node(head.val)

    def display(self):
        current = self.head
        while current is not None:
            print(current.val)
            current = current.next

    def insert(self,value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def insertToHead(self,value):
        newHead = Node(value)
        newHead.next=self.head
        self.head = newHead

    def size(self):
        len = 0
        if self.head is None:
            return len
        else:
            current = self.head
            while current.next is not None:
                current = current.next
                len += 1
            return len + 1


    def deleteHead(self):
        self.head = self.head.next

    def search(self,value):
        i=0
        current = self.head
        while current.val is not value and current.next is not None:
            i += 1
            current = current.next
            return -1
        return current.val, i



node1 = Node("hamzawey")
l = LinkedList(node1)
l.insert("hamza")
l.insertToHead("newHead")
l.display()
print(l.size())
l.deleteHead()
l.display()
print(l.size())
print (l.search("s"))
