class TreeNode:

    def __init__(self, value):
        self.data = value
        self.leftChild = None
        self.rightChild = None
        self.isDeleted = False

    def getData(self):
        return self.data

    def setLeftChild(self, leftChild):
        self.leftChild = leftChild

    def setRightChild(self, rightChild):
        self.rightChild = rightChild

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def insert(self,data):
        if data >= self.data:
            if self.rightChild is None:
                self.rightChild = TreeNode(data)
            else:
                self.rightChild.insert(data)
        else:
            if self.leftChild is None:
                self.leftChild = TreeNode(data)
            else:
                self.leftChild.insert(data)

    def delete(self):
        self.isDeleted = True

    def smallest(self):
        if self.getLeftChild() is None:
           return self.getData()
        return self.getLeftChild().smallest()

    def largest(self):
        if self.getRightChild() is None:
            return self.getData()
        return self.getRightChild().largest()

    def find(self,data):
        if self.data==data and not self.isDeleted:
            return self
        if self.data > data and self.leftChild is not None:
            return self.leftChild.find(data)
        if self.data < data and self.rightChild is not None:
            return self.rightChild.find(data)
        return None

    def inOrder(self):
        if self.leftChild:
            return self.leftChild.inOrder()
        print(self.data)
        if self.rightChild:
            return self.rightChild.inOrder()

    def inorderTraversal(self, root):
        res = []
        if root is not None:
            res = self.inorderTraversal(root.leftChild)
            res.append(root.data)
            res = res + self.inorderTraversal(root.rightChild)
        return res

    def preorderTraversal(self, root):
        res = []
        if root is not None:
            res.append(root.data)
            res = res +self.inorderTraversal(root.leftChild)
            res = res + self.inorderTraversal(root.rightChild)
        return res

    def postorderTraversal(self, root):
        res = []
        if root is not None:
            res = res + self.inorderTraversal(root.leftChild)
            res = res + self.inorderTraversal(root.rightChild)
            res.append(root.data)
        return res


class BinarySearchTree:

    """
    height of a BST log2(n)
    Search Complexity o(log2n)
    Delete Complexity o(log2n)
    """
    def __init__(self, root):
        self.root = root

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self.root.insert(data)

    def find(self, data):
        if self.root is not None:
            return self.root.find(data)
        return None

    def delete(self,data):
        toDel = self.find(data)
        toDel.delete()

    def smallest(self):
        if self.root is not None:
            return self.root.smallest()
        return None

    def largest(self):
        if self.root is not None:
            return self.root.largest()
        return None

    def inOrder(self):
        if self.root is not None:
            return self.root.inorderTraversal(self.root)
        return

    def preOrder(self):
        if self.root is not None:
            return self.root.preorderTraversal(self.root)
        return

    def postOrder(self):
        if self.root is not None:
            return self.root.postorderTraversal(self.root)
        return



    # def delete(self, data):
    #
    #     current = self.root
    #     parent = self.root
    #     isLeftChild = False
    #
    #     if current is None:
    #         return
    #     while current is not None and current.getData() !=data:
    #         parent = current
    #         if data < current.getData():
    #             current = current.getLeftChild()
    #             isLeftChild = True
    #         else:
    #             current = current.getRightChild()
    #             isLeftChild = False
    #
    #     if current is None:
    #         return
    #     if current.getLeftChild() is None and current.getRightChild() is None:
    #         if current == self.root:
    #             self.root = None
    #         else:
    #             if isLeftChild:
    #                 parent.setLeftChild(None)
    #             else:
    #                 parent.setRightChild(None)
    #
    #     elif current.getRightChild() is None:
    #         if current == self.root:
    #             self.root = current.getLeftChild()
    #         elif isLeftChild:
    #             parent.setLeftChild(current.getLeftChild())
    #         else:
    #             parent.setRightChild(current.getRightChild())
    #     elif current.getLeftChild() is None:
    #         if current == self.root:
    #             self.root = current.getRightChild()
    #         elif isLeftChild:
    #             parent.setLeftChild(current.getRightChild())
    #         else:
    #             parent.setRightChild(current.getLeftChild())






r = TreeNode(52)
x = BinarySearchTree(r)

x.insert(33)
x.insert(65)


#print (x.root.getRightChild().data)
#print (x.smallest())
#print (x.largest())

print(x.inOrder())
print(x.preOrder())
print(x.postOrder())



