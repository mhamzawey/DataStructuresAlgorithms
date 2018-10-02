from LinkedList import Node


class SortedLinkedList:
    def __init__(self, head):
        self.head = head

    def insert(self,val):
        """
        inserts data in order.  This would be a sorting algorithm of Complexity o(n)
        :param val:
        :return:
        """
        current = self.head
        new_node = Node(val)
        if current is None:
            self.head = new_node
            return
        elif current.val > val:
            new_node.next = current
            self.head = new_node
            return
        while current.next is not None:
            if current.next.val > val:
                break
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current is not None:
            print(current.val)
            current = current.next


head = Node(1)
x = SortedLinkedList(head)
x.insert(2)
x.insert(5)
x.insert(7)
x.insert(3)
x.insert(18)

x.display()

