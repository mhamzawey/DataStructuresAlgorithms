class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self,val):
        self.head = Node(val)

    def insert(self,val):
        current = self.head
        new_node = Node(val)
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def __len__(self):
        i = 0
        current = self.head
        while current.next is not None:
            i += 1
            current = current.next
        return i+1

    def __str__(self):
        data = []
        current = self.head
        while current is not None:
            data.append(current.val)
            current = current.next
        return str(data)


l=DoubleLinkedList(1)
l.insert(5)
l.insert(17)

print(l)
print(len(l))