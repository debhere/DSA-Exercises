'''
Demonstrating Traversals
'''

from Queue.QueueLinkedList import Queue


# Importing user-defined Queue implementation with Linked List for level order traversal


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# newBinaryTree = TreeNode('Drinks')
# leftChild = TreeNode('Hot')
# rightChild = TreeNode('Cold')
#
# leftToLeft = TreeNode('Tea')
# rightToLeft = TreeNode('Coffee')
# leftToRight = TreeNode('Thumps Up')
# rightToRight = TreeNode('Wine')
#
# newBinaryTree.left = leftChild
# newBinaryTree.right = rightChild
#
# leftChild.left = leftToLeft
# leftChild.right = rightToLeft
# rightChild.left = leftToRight
# rightChild.right = rightToRight


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        print(rootNode.data)
        preOrderTraversal(rootNode.left)
        preOrderTraversal(rootNode.right)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        inOrderTraversal(rootNode.left)
        print(rootNode.data)
        inOrderTraversal(rootNode.right)


def postOrderTraversal(root):
    if not root:
        return
    else:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        print(root.data)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        q = Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            root = q.dequeue()
            print(root.value.data)
            if root.value.left is not None:
                q.enqueue(root.value.left)
            if root.value.right is not None:
                q.enqueue(root.value.right)


def searchBinaryTree(rootNode, searchValue):
    isFound = False
    if rootNode is None:
        isFound = False
    else:
        q = Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            root = q.dequeue()
            if root.value.data == searchValue:
                isFound = True
            else:
                if root.value.left is not None:
                    q.enqueue(root.value.left)
                if root.value.right is not None:
                    q.enqueue(root.value.right)
        return isFound


def insertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
        return "Success"
    else:
        q = Queue()
        q.enqueue(rootNode)
        while not q.isEmpty():
            root = q.dequeue()
            if root.value.left is not None:
                q.enqueue(root.value.left)
            else:
                root.value.left = newNode
                return "Success"
            if root.value.right is not None:
                q.enqueue(root.value.right)
            else:
                root.value.right = newNode
                return "Success"


# preOrderTraversal(newBinaryTree)
# inOrderTraversal(newBinaryTree)
# postOrderTraversal(newBinaryTree)
# levelOrderTraversal(newBinaryTree)

# print(searchBinaryTree(newBinaryTree, 'Coffee'))
# print(searchBinaryTree(newBinaryTree, 'Beer'))

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)

t1.left = t2
t1.right = t3

insertNode(t1, t4)
insertNode(t1, t5)
levelOrderTraversal(t1)
