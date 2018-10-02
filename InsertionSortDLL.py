from DoubleLinkedList import Node
from DoubleLinkedList import DoubleLinkedList


def sort(l):
    print("started sorting")
    if len(l) == 0:
        return False
    else:
        current = l.head

    while current.next is not None:
        if current.val <= current.next.val:
            current = current.next
        else:
            temp = current.prev
            current.prev = current





l = DoubleLinkedList(12)
l.insert(10)
l.insert(1)
l.insert(3)
l.insert(2)
l.insert(6)
print(l)
sort(l)
print(l)
